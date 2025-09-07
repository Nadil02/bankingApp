from fastapi import FastAPI
from routes import chatbot  
from routes.bankAccountManagement import router as bankAccountManagementRouter
from routes.todo import router as todo_router
from routes.dashboard import router as dashboard_router
from routes import user_login  # import the combined router from routes.py
from routes import sign_in, forgot_password,transaction_categorization
from routes import sign_in, forgot_password, transaction_history
from routes import sign_in, forgot_password,change_password, settings, incomeExpensePredictions
from routes import notification
from services.notification_watcher import watch_notifications
from fastapi.middleware.cors import CORSMiddleware
import asyncio
from services.websocket_manager import websocket_manager

# initialize FastAPI app
app = FastAPI()

app.include_router(chatbot.router)
app.include_router(bankAccountManagementRouter)
app.include_router(todo_router)
app.include_router(dashboard_router)
app.include_router(user_login.router)
app.include_router(sign_in.router)
app.include_router(forgot_password.router)
app.include_router(transaction_categorization.router)
app.include_router(transaction_history.router)
app.include_router(change_password.router)
app.include_router(settings.router)
app.include_router(incomeExpensePredictions.router)
app.include_router(notification.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup_event():
    asyncio.create_task(watch_notifications())

@app.get("/health")
def health_check():
    return {"status": "okks"}


