from fastapi import FastAPI
from routes import chatbot  

# initialize FastAPI app
app = FastAPI()

# include the routes from the routes folder
app.include_router(chatbot.router)
