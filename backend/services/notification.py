from database import collection_notification, collection_expo_tokens, collection_account
from schemas.notification import Notification
from datetime import datetime

async def fetch_notifications_with_account(user_id: int):
    notifications = await collection_notification.find(
        {"user_id": user_id}
    ).sort("created_at", -1).to_list(length=None)

    for notif in notifications:
        notif["_id"] = str(notif["_id"])
        if notif.get("account_id"):
            account = await collection_account.find_one({"account_id": notif["account_id"]})
            if account:
                notif["account_number"] = account["account_number"]
                notif["account_type"] = account["account_type"]
                notif["bank_id"] = account["bank_id"]
    return notifications


async def create_and_return_notification(notification: Notification):
    notification_dict = notification.dict()
    notification_dict["created_at"] = datetime.utcnow()

    if notification_dict.get("account_id"):
        account = await collection_account.find_one({"account_id": notification_dict["account_id"]})
        if account:
            notification_dict["account_number"] = account["account_number"]
            notification_dict["account_type"] = account["account_type"]
            notification_dict["bank_id"] = account["bank_id"]

    result = await collection_notification.insert_one(notification_dict)
    notification_dict["_id"] = str(result.inserted_id)
    return notification_dict


async def get_unread_count(user_id: int):
    return await collection_notification.count_documents({
        "user_id": user_id,
        "seen": False
    })


async def mark_all_seen(user_id: int):
    await collection_notification.update_many(
        {"user_id": user_id, "seen": False},
        {"$set": {"seen": True}}
    )


async def save_expo_token(user_id: int, token: str):
    await collection_expo_tokens.update_one(
        {"user_id": user_id},
        {"$set": {"token": token}},
        upsert=True
    )
