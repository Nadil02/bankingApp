from fastapi import FastAPI
from routes import user_login

# initialize FastAPI app
app = FastAPI()

# include the routes from the routes.py file
app.include_router(user_login.router)
