from fastapi import FastAPI
from routes import sign_in, forgot_password

# initialize FastAPI app
app = FastAPI()

# include the routes from the routes.py file
app.include_router(sign_in.router)
app.include_router(forgot_password.router)
