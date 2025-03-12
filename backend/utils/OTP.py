import httpx
import os

# Load your credentials from environment variables or directly assign them
USER_ID = os.getenv("NOTIFY_LK_USER_ID", "29160")
API_KEY = os.getenv("NOTIFY_LK_API_KEY", "0M2hBE8wyTVkIV40pfRN")
SENDER_ID = os.getenv("NOTIFY_LK_SENDER_ID", "NotifyDEMO")  # Use your approved sender ID
BASE_URL = "https://app.notify.lk/api/v1"

def send_sms(to: str, message: str):
    """Send an SMS using Notify.lk API."""
    print("Sending SMS to", to)
    url = f"{BASE_URL}/send"
    params = {
        "user_id": USER_ID,
        "api_key": API_KEY,
        "sender_id": SENDER_ID,
        "to": to,
        "message": message,
    }
    response = httpx.get(url, params=params)
    print(response.json())
    print(account_status())
    return response.json()

def account_status():
    """Check account status and balance."""
    url = f"{BASE_URL}/status"
    params = {
        "user_id": USER_ID,
        "api_key": API_KEY,
    }
    response = httpx.get(url, params=params)
    return response.json()