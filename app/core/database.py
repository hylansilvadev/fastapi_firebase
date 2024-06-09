import firebase_admin
from fastapi import HTTPException
from firebase_admin import credentials, firestore, initialize_app

from app.core.config import settings


doc_cred = {
    "type": f"{settings.TYPE}",
    "project_id": f"{settings.PROJECT_ID}",
    "private_key_id": f"{settings.PRIVATE_KEY_ID}",
    "private_key": f"{settings.PRIVATE_KEY}",
    "client_email": f"{settings.CLIENT_EMAIL}",
    "client_id": f"{settings.CLIENT_ID}",
    "auth_uri": f"{settings.AUTH_URI}",
    "token_uri": f"{settings.TOKEN_URI}",
    "auth_provider_x509_cert_url": f"{settings.AUTH_PROVIDER_X509_CERT_URL}",
    "client_x509_cert_url": f"{settings.CLIENT_X509_CERT_URL}",
    "universe_domain": f"{settings.UNIVERSE_DOMAIN}"
}

try:
    cred = credentials.Certificate(doc_cred)
    initialize_app(cred)
except firebase_admin.exceptions.FirebaseError as e:
    raise HTTPException(
        status_code=500, detail=f"Firebase initialization error: {e}"
    )

database = firestore.client()
