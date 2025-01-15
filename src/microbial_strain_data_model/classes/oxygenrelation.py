from typing_extensions import Annotated
from pydantic import BaseModel, ConfigDict, Field, StringConstraints


class OxygenRelation(BaseModel):
    """OxygenRelation of the strain"""

    model_config = ConfigDict(
        strict=True,
        extra="forbid",
        revalidate_instances="always",
        str_strip_whitespace=True,
    )

    relation: str = Field(title="Oxygen Relation", alias="oxygenRelation")
    source: Annotated[str, StringConstraints(pattern=r"^\/sources\/\d+$")] = Field(
        title="Source", alias="source", description="JSON path to source object"
    )
