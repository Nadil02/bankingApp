from fastapi import FastAPI
from routes.todo import router as todo_router

# initialize FastAPI app
app = FastAPI()

# include the routes from the routes.py file
app.include_router(todo_router)
