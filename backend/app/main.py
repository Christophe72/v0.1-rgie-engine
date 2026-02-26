from pathlib import Path
import sys
from contextlib import asynccontextmanager

from fastapi import FastAPI
from sqlalchemy import text

if __package__ is None or __package__ == "":
    project_root = Path(__file__).resolve().parents[1]
    if str(project_root) not in sys.path:
        sys.path.insert(0, str(project_root))

from app.database import Base, SessionLocal, engine
from app.routers import health, rules
from app.seed import seed_database


with engine.begin() as conn:
    conn.execute(text("CREATE SCHEMA IF NOT EXISTS rgie"))

Base.metadata.create_all(bind=engine)

@asynccontextmanager
async def lifespan(_: FastAPI):
    db = SessionLocal()
    try:
        seed_database(db)
        yield
    finally:
        db.close()


app = FastAPI(title="WebElec RGIE Engine", lifespan=lifespan)


app.include_router(health.router)
app.include_router(rules.router)