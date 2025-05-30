from fastapi import FastAPI
from sqlalchemy.exc import OperationalError
from sqlalchemy.orm import Session
import time
from app.database import engine, Base
from app.routes import client, ops

# Wait for the database to be ready
MAX_TRIES = 10
for attempt in range(MAX_TRIES):
    try:
        Base.metadata.create_all(bind=engine)
        print("Database ready!")
        break
    except OperationalError:
        print(f"Waiting for database(attempt {attempt + 1})")
        time.sleep(2)
else:
    raise RuntimeError("Could not connect to database ")

app = FastAPI(title="Secure File Sharing")
app.include_router(client.router, prefix="/client", tags=["Client"])
app.include_router(ops.router, prefix="/ops", tags=["Ops"])
