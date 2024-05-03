import firebase_admin
from fastapi import HTTPException
from firebase_admin import credentials, firestore, initialize_app

from app.core.config import settings

try:
    cred = credentials.Certificate(settings.SECRET_DATABASE_PATH)
    initialize_app(cred)
except firebase_admin.exceptions.FirebaseError as e:
    raise HTTPException(
        status_code=500, detail=f'Firebase initialization error: {e}'
    )

database = firestore.client()
