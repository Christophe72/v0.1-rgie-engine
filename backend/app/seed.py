from sqlalchemy.orm import Session
from app import models

RGIE_2025_SEED = [
    {
        "code": "R1",
        "title": "Schéma unifilaire obligatoire",
        "description": "Toute installation domestique doit disposer d’un schéma unifilaire conforme.",
        "legal_reference": "Chapitre 2.12",
        "is_new": True,
        "metadata": {"version": "2025.03"}
    },
    {
        "code": "R2",
        "title": "Protection différentielle 300 mA",
        "description": "Protection générale incendie obligatoire.",
        "legal_reference": "Partie 4",
        "is_new": False,
        "metadata": {"type": "protection"}
    }
]
def seed_database(db: Session):
    existing_codes = {
        row[0] for row in db.query(models.Rule.code).all()
    }

    inserted = 0
    for rule_data in RGIE_2025_SEED:
        if rule_data["code"] in existing_codes:
            continue

        payload = dict(rule_data)
        payload["rule_metadata"] = payload.pop("metadata", None)

        rule = models.Rule(**payload)
        db.add(rule)
        inserted += 1

    if inserted > 0:
        db.commit()
        print(f"RGIE 2025 seed loaded ({inserted} rule(s) added).")