from fastapi import FastAPI, HTTPException
from .models import PasswordItemBase, PasswordItemOut
import logging

from .storage import PasswordStorage

logger = logging.getLogger(__name__)

app = FastAPI()

storage = PasswordStorage()


@app.post("/passwords/")
def create_password_item(item: PasswordItemBase):
    logger.info(f"password item: {item}")
    storage.save_password(item)
    return {"message": "ok"}


@app.get("/passwords/")
def get_passwords():
    result = []
    for v in storage.get_passwords():
        result.append(v)

    return result


@app.get("/passwords/{item_id}")
def get_password(item_id: str) -> PasswordItemOut:
    password = storage.get_password(item_id)
    if password is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return password
