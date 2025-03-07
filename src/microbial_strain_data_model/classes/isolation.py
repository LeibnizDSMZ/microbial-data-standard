from typing_extensions import Annotated
from pydantic import BaseModel, ConfigDict, Field, StringConstraints

from microbial_strain_data_model.classes.actors import Organization, Person
from microbial_strain_data_model.classes.sourcestring import SourceString


class Isolation(BaseModel):
    """Isolation event information"""

    model_config = ConfigDict(
        strict=True,
        extra="forbid",
        revalidate_instances="always",
        str_strip_whitespace=True,
    )

    date: (
        Annotated[
            str,
            StringConstraints(
                strip_whitespace=True,
                to_upper=True,
                pattern=r"^(?:\d{4}[-\._]?\d{0,2}[-\._]?\d{0,2})?/?(?:\d{4}[-\._]?\d{0,2}[-\._]?\d{0,2})?$",
            ),
        ]
        | None
    ) = Field(default=None, title="Date")
    isolatedAt: Organization | Person | None = Field(default=None, title="Isolated At")
    source: list[SourceString] = Field(
        title="Source", description="List of JSON paths to source object"
    )
