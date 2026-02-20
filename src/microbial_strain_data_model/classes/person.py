from pydantic import BaseModel, ConfigDict, Field
from microbial_strain_data_model.classes.identifier import Identifier


class Person(BaseModel):
    """Person."""

    model_config = ConfigDict(
        strict=True,
        extra="forbid",
        revalidate_instances="always",
        str_strip_whitespace=True,
    )

    name: str = Field(
        title="Name", description="Name of the person, preferable: [Last], [First]"
    )
    identifier: list[Identifier] = Field(
        default_factory=list,
        title="Identifier",
        description="Person identifiers like ORCID",
    )
