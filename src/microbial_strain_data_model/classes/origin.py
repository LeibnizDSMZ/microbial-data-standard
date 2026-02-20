from typing_extensions import Annotated
from pydantic import BaseModel, ConfigDict, Field, StringConstraints

from microbial_strain_data_model.classes.country import Country
from microbial_strain_data_model.classes.isolationtag import IsolationTag
from microbial_strain_data_model.classes.location import Location
from microbial_strain_data_model.classes.organization import Organization
from microbial_strain_data_model.classes.links import SourceLink
from microbial_strain_data_model.classes.person import Person


class Origin(BaseModel):
    """Isolation event information.

    Notes:
        - Sample = The material probe in which the strain was found
        - Isolation = Isolation of the strain from the sample
    """

    model_config = ConfigDict(
        strict=True,
        extra="forbid",
        revalidate_instances="always",
        str_strip_whitespace=True,
    )

    sampleDate: (
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
        description="Date of sampling, using date range format of dublin core: "
        "'YYYY-MM-DD/YYYY-MM-DD' ether side can be empty defining an open ended "
        "range, only the year is mandatory, e.g. '/1978' means before 1978",
    )
    country: Country | None = Field(
        default=None,
        title="Country",
        description="Country where the sample material originated from",
    )
    description: str | None = Field(
        default=None, title="Description", description="Description of the sample"
    )
    locationCreated: Location | None = Field(
        default=None,
        title="Location Created",
        description="Location where the sample was taken",
    )
    tags: list[IsolationTag] = Field(default_factory=list, title="Isolation Source Tags")
    sampler: Person | None = Field(
        default=None, title="Sampler", description="Person that sampled the material"
    )
    isolationDate: (
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
        description="Date of isolation from the sample material, using date range format"
        " of dublin core:'YYYY-MM-DD/YYYY-MM-DD' ether side can be empty defining an open"
        " ended range, only the year is mandatory, e.g. '/1978' means before 1978",
    )
    isolatedAt: Organization | None = Field(
        default=None,
        title="Isolated At",
        description="Institute where the strain was isolated from the sample",
    )
    isolator: Person | None = Field(
        default=None,
        title="Isolator",
        description="Person that isolated the strain from the sample",
    )
    source: list[SourceLink] = Field(
        title="Source", description="List of JSON paths to source object"
    )
