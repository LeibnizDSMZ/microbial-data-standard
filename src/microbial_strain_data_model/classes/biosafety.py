from pydantic import BaseModel, ConfigDict, Field, HttpUrl

from microbial_strain_data_model.classes.sourcestring import SourceString


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
    source: list[SourceString] = Field(
        title="Source", alias="source", description="List of JSON paths to source object"
    )
