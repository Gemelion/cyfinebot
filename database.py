from datetime import datetime

# Заглушка: в реальном приложении используем БД с шифрованием
USERS_DB = {}

async def add_user(user_id, username, first_name, consent_date: datetime):
    USERS_DB[user_id] = {
        "username": username,
        "first_name": first_name,
        "consent_date": consent_date,
        "document": None,
        "vehicles": []
    }

async def user_exists(user_id) -> bool:
    return user_id in USERS_DB
