import firebase_admin
from fastapi import HTTPException
from firebase_admin import credentials, firestore, initialize_app

from app.core.config import settings


doc_cred = {
    "type": f"{settings.type}",
    "project_id": f"{settings.project_id}",
    "private_key_id": f"{settings.private_key_id}",
    "private_key": f"{settings.private_key}",
    "client_email": f"{settings.client_email}",
    "client_id": f"{settings.client_id}",
    "auth_uri": f"{settings.auth_uri}",
    "token_uri": f"{settings.token_uri}",
    "auth_provider_x509_cert_url": f"{settings.auth_provider_x509_cert_url}",
    "client_x509_cert_url": f"{settings.auth_provider_x509_cert_url}",
    "universe_domain": f"{settings.universe_domain}"
}

try:
    cred = credentials.Certificate(doc_cred)
    initialize_app(cred)
except firebase_admin.exceptions.FirebaseError as e:
    raise HTTPException(
        status_code=500, detail=f"Firebase initialization error: {e}"
    )

database = firestore.client()
