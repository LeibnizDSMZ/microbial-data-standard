from typing_extensions import Annotated
from pydantic import BaseModel, StringConstraints, Field, HttpUrl


class Enzyme(BaseModel):
    """Information about one enzyme"""

    name: str | None = Field(default=None, title="Name", alias="name")
    ec_num: Annotated[
        str,
        StringConstraints(
            strip_whitespace=True, to_upper=True, pattern=r"(?:EC)? ?\d+\.\d+\.\d+\.n?\d+"
        ),
    ] = Field(
        title="EC Number",
        alias="hasECNumber",
        description="An EC number like defined by the Enzyme Commission",
    )
    url: HttpUrl | None = Field(default=None, title="URL", alias="url", description="URL")
    alternate_name: list[str] = Field(
        default_factory=list, title="Alternate Name", alias="alternateName"
    )
    active: bool | None = Field(default=None, title="Active", alias="active")
    source: Annotated[str, StringConstraints(pattern=r"^\/sources\/\d+$")] = Field(
        title="Source", alias="source", description="JSON path to source object"
    )
