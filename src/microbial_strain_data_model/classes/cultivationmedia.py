from pydantic import BaseModel, ConfigDict, Field, HttpUrl

from microbial_strain_data_model.classes.sourcestring import SourceString


class CultivationMedia(BaseModel):
    """Cultivation media, use links to Media Dive or other resources"""

    model_config = ConfigDict(
        strict=True,
        extra="forbid",
        revalidate_instances="always",
        str_strip_whitespace=True,
    )

    name: str = Field(title="Name", alias="name")
    url: HttpUrl | None = Field(default=None, title="URL", alias="url")
    reagents: list[str] = Field(
        default_factory=list, title="Reagent Used", alias="reagentUsed"
    )
    source: list[SourceString] = Field(
        title="Source", alias="source", description="List of JSON paths to source object"
    )
