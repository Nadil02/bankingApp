from fastapi import FastAPI
from routes.bankAccountManagement import router as bankAccountManagementRouter

# initialize FastAPI app
app = FastAPI()

# include the routes from the routes.py file
app.include_router(bankAccountManagementRouter)
