from fastapi import FastAPI
from routes import router  # import the combined router from routes.py

# initialize FastAPI app
app = FastAPI()

# include the routes from the routes.py file
app.include_router(router)
