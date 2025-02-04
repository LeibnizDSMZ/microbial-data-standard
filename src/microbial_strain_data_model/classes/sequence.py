from pydantic import BaseModel, ConfigDict, Field, HttpUrl

from microbial_strain_data_model.classes.enums import SequenceLevel, SequenceType

from microbial_strain_data_model.classes.sourcestring import SourceString


class Sequence(BaseModel):
    """Information on a Sequence"""

    model_config = ConfigDict(
        strict=True,
        extra="forbid",
        revalidate_instances="always",
        str_strip_whitespace=True,
    )

    type: SequenceType = Field(title="Type", alias="type")
    level: SequenceLevel = Field(title="Level", alias="level")
    accession: str = Field(title="Accession Number", alias="accessionNumber")
    description: str | None = Field(
        default=None, title="Description", alias="description"
    )
    length: str | None = Field(default=None, title="Length", alias="length")
    url: list[HttpUrl] = Field(default_factory=list, title="URL", alias="url")
    source: list[SourceString] = Field(
        title="Source", alias="source", description="List of JSON paths to source object"
    )
