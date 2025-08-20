from typing_extensions import Annotated
from pydantic import BaseModel, ConfigDict, StringConstraints, Field

from microbial_strain_data_model.classes.identifier import Identifier
from microbial_strain_data_model.classes.links import RelationLink, SourceLink


class Enzyme(BaseModel):
    """Information about one enzyme"""

    model_config = ConfigDict(
        strict=True,
        extra="forbid",
        revalidate_instances="always",
        str_strip_whitespace=True,
    )

    name: str | None = Field(default=None, title="Name")
    hasECNumber: Annotated[
        str,
        StringConstraints(
            strip_whitespace=True, to_upper=True, pattern=r"(?:EC)? ?\d+\.\d+\.\d+\.n?\d+"
        ),
    ] = Field(
        title="EC Number",
        description="An EC number defined by the Enzyme Commission",
    )
    identifier: list[Identifier] = Field(default_factory=list, title="Identifier")
    alternateName: list[str] = Field(default_factory=list, title="Alternate Name")
    active: bool | None = Field(
        default=None, title="Active", description="Is this enzyme active"
    )
    relatedData: list[RelationLink] = Field(
        default_factory=list,
        title="Related Data",
        description="JSON paths to relation object",
    )
    source: list[SourceLink] = Field(
        title="Source", description="List of JSON paths to source object"
    )
