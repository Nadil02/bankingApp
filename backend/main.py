from fastapi import FastAPI
from routes.todo import router as todo_router
from routes.dashboard import router as dashboard_router
from routes import user_login  # import the combined router from routes.py
from routes import sign_in, forgot_password,change_password, settings


# initialize FastAPI app
app = FastAPI()

# include the routes from the routes.py file
app.include_router(todo_router)
app.include_router(dashboard_router)
app.include_router(user_login.router)
app.include_router(sign_in.router)
app.include_router(forgot_password.router)
app.include_router(change_password.router)
app.include_router(settings.router)

