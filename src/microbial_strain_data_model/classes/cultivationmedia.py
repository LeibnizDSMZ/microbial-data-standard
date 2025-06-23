from pydantic import BaseModel, ConfigDict, Field, HttpUrl

from microbial_strain_data_model.classes.links import SourceLink


class CultivationMedia(BaseModel):
    """Cultivation media, use links to Media Dive or other resources"""

    model_config = ConfigDict(
        strict=True,
        extra="forbid",
        revalidate_instances="always",
        str_strip_whitespace=True,
    )

    name: str = Field(title="Name")
    url: HttpUrl | None = Field(default=None, title="URL")
    reagentUsed: list[str] = Field(default_factory=list, title="Reagent Used")
    source: list[SourceLink] = Field(
        title="Source", description="List of JSON paths to source object"
    )
