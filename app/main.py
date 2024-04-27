from fastapi import FastAPI

from app.api.router import router

app = FastAPI(
    title='FastAPI + Firebase (firebase_admin & firedantic)', docs_url='/'
)


app.include_router(router)
