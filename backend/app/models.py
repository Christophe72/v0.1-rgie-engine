from sqlalchemy import Column, String, Boolean
from sqlalchemy.dialects.postgresql import UUID, JSONB
import uuid
from app.database import Base

class Rule(Base):
    __tablename__ = "rules"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    code = Column(String, unique=True, nullable=False)
    title = Column(String, nullable=False)
    description = Column(String)
    legal_reference = Column(String)
    is_new = Column(Boolean, default=False)
    rule_metadata = Column("metadata", JSONB)