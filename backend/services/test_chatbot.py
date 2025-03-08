import asyncio
from services.llmAgentTools import chatbot_system_answer

# The chatbot_system_answer function is already defined above

async def test_chatbot_system_answer():
    query = "What is the purpose of the system?"  # Example query
    response = await chatbot_system_answer(query)
    print("Response from chatbot system:", response)

# Run the test function
asyncio.run(test_chatbot_system_answer())
