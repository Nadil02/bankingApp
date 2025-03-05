from fastapi import FastAPI
# from routes import router  # import the combined router from routes.py
from routes.dashboard import router as dashboard_router

# initialize FastAPI app
app = FastAPI()

# include the routes from the routes.py file
app.include_router(dashboard_router)
