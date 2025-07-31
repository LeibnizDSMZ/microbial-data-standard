from typing_extensions import Annotated
from pydantic import BaseModel, ConfigDict, Field, StringConstraints

from microbial_strain_data_model.classes.organization import Organization
from microbial_strain_data_model.classes.links import SourceLink


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
    ) = Field(
        default=None,
        title="Date",
        description="Date of Isolation, using date range format of dublin core: "
        "'YYYY-MM-DD/YYYY-MM-DD' ether side can be empty defining an open ended "
        "range, only the year is mandatory, e.g. '/1978' means before 1978",
    )
    isolatedAt: Organization | None = Field(
        default=None,
        title="Isolated At",
        description="Institute where the isolation happened",
    )
    source: list[SourceLink] = Field(
        title="Source", description="List of JSON paths to source object"
    )
