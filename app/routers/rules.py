from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app import models, schemas

router = APIRouter(prefix="/rules", tags=["Rules"])


def _serialize_rule(rule: models.Rule) -> dict:
    return {
        "id": rule.id,
        "code": rule.code,
        "title": rule.title,
        "description": rule.description,
        "legal_reference": rule.legal_reference,
        "is_new": rule.is_new,
        "metadata": rule.rule_metadata,
    }

@router.get("/", response_model=list[schemas.RuleResponse])
def get_rules(db: Session = Depends(get_db)):
    rules = db.query(models.Rule).all()
    return [_serialize_rule(rule) for rule in rules]

@router.post("/", response_model=schemas.RuleResponse)
def create_rule(rule: schemas.RuleCreate, db: Session = Depends(get_db)):
    db_rule = models.Rule(**rule.model_dump())
    db.add(db_rule)
    db.commit()
    db.refresh(db_rule)
    return _serialize_rule(db_rule)