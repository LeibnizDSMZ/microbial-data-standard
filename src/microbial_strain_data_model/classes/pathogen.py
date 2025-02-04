from pydantic import BaseModel, ConfigDict, Field

from microbial_strain_data_model.classes.enums import Host, PathogenLevel

from microbial_strain_data_model.classes.sourcestring import SourceString


class Pathogen(BaseModel):
    """Pathogen, defining Host, pathogenicity and under what classification"""

    model_config = ConfigDict(
        strict=True,
        extra="forbid",
        revalidate_instances="always",
        str_strip_whitespace=True,
    )

    host: Host = Field(title="Host", alias="host")
    pathogen: PathogenLevel = Field(title="Pathogen", alias="pathogen")
    classification: str | None = Field(
        default=None, title="Classification", alias="classification"
    )
    source: list[SourceString] = Field(
        title="Source", alias="source", description="List of JSON paths to source object"
    )
