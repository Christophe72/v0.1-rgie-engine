from fastapi import FastAPI
from sqlalchemy import text
from app.database import Base, engine
from app.routers import rules, health

with engine.begin() as conn:
	conn.execute(text("CREATE SCHEMA IF NOT EXISTS rgie"))

Base.metadata.create_all(bind=engine)

app = FastAPI(title="WebElec RGIE Engine")

app.include_router(health.router)
app.include_router(rules.router)