from typing_extensions import Annotated
from pydantic import BaseModel, Field, HttpUrl, StringConstraints


class BioSafety(BaseModel):
    """Biosafety classification"""

    group: str = Field(title="Riskgroup", alias="riskgroup")
    classification: str | None = Field(
        default=None, title="Classification", alias="classification"
    )
    url: HttpUrl | None = Field(default=None, title="URL", alias="url")
    source: Annotated[str, StringConstraints(pattern=r"^\/sources\/\d+$")] = Field(
        title="Source", alias="source", description="JSON path to source object"
    )
