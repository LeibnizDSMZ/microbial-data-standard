from typing_extensions import Annotated
from pydantic import BaseModel, ConfigDict, Field, HttpUrl, StringConstraints


class BioSafety(BaseModel):
    """Biosafety classification"""

    model_config = ConfigDict(
        strict=True,
        extra="forbid",
        revalidate_instances="always",
        str_strip_whitespace=True,
    )

    group: str = Field(title="Riskgroup", alias="riskgroup")
    classification: str | None = Field(
        default=None, title="Classification", alias="classification"
    )
    url: HttpUrl | None = Field(default=None, title="URL", alias="url")
    source: Annotated[str, StringConstraints(pattern=r"^\/sources\/\d+$")] = Field(
        title="Source", alias="source", description="JSON path to source object"
    )
