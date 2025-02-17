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

    host: Host = Field(title="Host")
    pathogen: PathogenLevel = Field(title="Pathogen")
    classification: str | None = Field(default=None, title="Classification")
    source: list[SourceString] = Field(
        title="Source", description="List of JSON paths to source object"
    )
