from pydantic import BaseModel, ConfigDict, Field

from microbial_strain_data_model.classes.enums import SequenceLevel, SequenceType
from microbial_strain_data_model.classes.identifier import Identifier
from microbial_strain_data_model.classes.sourcestring import SourceString


class Sequence(BaseModel):
    """Information on a Sequence"""

    model_config = ConfigDict(
        strict=True,
        extra="forbid",
        revalidate_instances="always",
        str_strip_whitespace=True,
    )

    type: SequenceType = Field(title="Type")
    level: SequenceLevel = Field(title="Level")
    accessionNumber: str = Field(title="Accession Number")
    description: str | None = Field(default=None, title="Description")
    length: str | None = Field(default=None, title="Length")
    identifier: list[Identifier] = Field(default_factory=list, title="Identifier")
    source: list[SourceString] = Field(
        title="Source", description="List of JSON paths to source object"
    )
