from typing_extensions import Annotated
from pydantic import BaseModel, Field, StringConstraints

from microbial_strain_data_model.classes.actors import Organization, Person


class Isolation(BaseModel):
    """Isolation event information"""

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
    ) = Field(default=None, title="Date", alias="date")
    isolator: Organization | Person | None = Field(
        default=None, title="Isolated At", alias="isolatedAt"
    )
    source: Annotated[str, StringConstraints(pattern=r"^\/sources\/\d+$")] = Field(
        title="Source", alias="source", description="JSON path to source object"
    )
