from typing_extensions import Annotated
from pydantic import BaseModel, Field, HttpUrl, StringConstraints


class CultivationMedia(BaseModel):
    """Cultivation media, use links to Media Dive or other resources"""

    name: str | None = Field(default=None, title="Name", alias="name")
    url: HttpUrl | None = Field(title="URL", alias="url")
    reagents: list[str] = Field(
        default_factory=list, title="Reagent Used", alias="reagentUsed"
    )
    source: Annotated[str, StringConstraints(pattern=r"^\/sources\/\d+$")] = Field(
        title="Source", alias="source", description="JSON path to source object"
    )
