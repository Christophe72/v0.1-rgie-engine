from pydantic import BaseModel
from pydantic import ConfigDict, Field
from uuid import UUID
from typing import Optional, Dict

class RuleBase(BaseModel):
    code: str
    title: str
    description: Optional[str]
    legal_reference: Optional[str]
    is_new: Optional[bool] = False
    rule_metadata: Optional[Dict] = Field(
        default=None,
        validation_alias="metadata",
        serialization_alias="metadata",
    )
    model_config = ConfigDict(populate_by_name=True)

class RuleCreate(RuleBase):
    pass

class RuleResponse(RuleBase):
    id: UUID

    model_config = ConfigDict(from_attributes=True, populate_by_name=True)