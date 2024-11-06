from typing_extensions import Annotated
from pydantic import BaseModel, Field, StringConstraints


class OxygenRelation(BaseModel):
    """OxygenRelation of the strain"""

    relation: str = Field(title="Oxygen Relation", alias="oxygenRelation")
    source: Annotated[str, StringConstraints(pattern=r"^\/sources\/\d+$")] = Field(
        title="Source", alias="source", description="JSON path to source object"
    )
