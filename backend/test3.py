from collections import Counter
from datetime import datetime
from database import collection_chatbot
from services.chatbotTest import get_new_summary, get_chat_summary, agent_executor, update_chat_summary, tools

# Function to handle greeting and suggest the most used tool
async def get_greeting_response(user_id: int) -> str:
    # Fetch the tool history for the user
    user_data = await collection_chatbot.find_one({"user_id": str(user_id)})
    
    if not user_data or "tool_history" not in user_data:
        return "Hello! How can I assist you today?"
    
    tool_history = user_data["tool_history"]
    
    # Extract tool names from the tool history
    tool_names = [tool["tool_name"] for tool in tool_history]
    
    if not tool_names:
        return "Hello! How can I assist you today?"
    
    # Find the most common tool
    tool_counter = Counter(tool_names)
    most_common_tool, _ = tool_counter.most_common(1)[0]
    
    # Create a response based on the most common tool
    response = f"Hello! Do you like to know about the {most_common_tool}?"
    
    return response


# Main function to handle chatbot responses
async def get_chatbot_response(user_id: int, query: str) -> str:
    # Check if the query is a greeting
    if query.lower() in ["hi", "hello", "hey", "hola"]:
        return await get_greeting_response(user_id)

    about_user = await get_chat_summary(user_id)
    
    enriched_query = f"User profile: {about_user}\n\nQuery: {query}\n\nUser ID: {user_id}"

    # Assuming agent_executor is tied to a specific tool (e.g., get_next_month_total_spendings)
    response = await agent_executor.ainvoke({
        "input": enriched_query
    })
    
    new_summary = get_new_summary(query, about_user)
    await update_chat_summary(user_id, new_summary)

    # Find the tool name based on the function being called
    tool_name = None
    for tool in tools:
        if callable(tool.func) and tool.func == agent_executor.name:
            tool_name = tool.name
            break

    if tool_name is None:
        # In case no tool is found, set a default tool name or log an error
        tool_name = "Unknown Tool"

    # Log tool usage in MongoDB
    tool_usage = {
        "tool_name": tool_name,  # Use the tool name from the tools list
        "timestamp": datetime.utcnow(),
        "query": query,
        "response": response["output"]
    }
    
    # Update the existing document with user_id and add to tool_history
    collection_chatbot.update_one(
        {"user_id": str(user_id)},  # Find the document by user_id
        {"$push": {"tool_history": tool_usage}}  # Push to the tool_history array
    )

    return response["output"]


import asyncio

# Assuming you have the user_id and query
user_id = 1  # Example user_id
query = "Hello"   # Example query

# Define the test function
async def test():
    response = await get_chatbot_response(user_id, query)
    print(response)

# Run the test coroutine
asyncio.run(test())