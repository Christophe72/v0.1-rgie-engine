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
    existing = db.query(models.Rule).count()
    if existing > 0:
        return  # évite double insertion

    for rule_data in RGIE_2025_SEED:
        rule = models.Rule(**rule_data)
        db.add(rule)

    db.commit()
    print("RGIE 2025 seed loaded.")