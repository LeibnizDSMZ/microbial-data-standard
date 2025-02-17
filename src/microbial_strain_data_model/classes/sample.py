from typing_extensions import Annotated, Self
from pydantic import BaseModel, ConfigDict, Field, StringConstraints, model_validator
from anytree.resolver import Resolver, ChildResolverError

from microbial_strain_data_model.data.isolation_sources_tree import root
from microbial_strain_data_model.classes.country import Country
from microbial_strain_data_model.classes.location import Location

from microbial_strain_data_model.classes.sourcestring import SourceString


class IsolationTag(BaseModel):
    """Isolation tag system, original used by BacDive"""

    model_config = ConfigDict(
        strict=True,
        extra="forbid",
        revalidate_instances="always",
        str_strip_whitespace=True,
    )

    level1: str = Field(title="Level 1")
    level2: str | None = Field(default=None, title="Level 2")
    level3: str | None = Field(default=None, title="Level 3")

    @model_validator(mode="after")
    def check_isolation_tag(self) -> Self:
        resolver = Resolver("name")
        path = "" + self.level1
        for x in [self.level2, self.level3]:
            if isinstance(x, str):
                path += "/"
                path += x
        try:
            resolver.get(root, path)
        except ChildResolverError as e:
            raise ValueError from ValueError(
                f"Isolation Source Tags are not valid isolation tag path: {e}"
            )
        return self


class Sample(BaseModel):
    """Information on the Sampling event of that Strain"""

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
    country: Country | None = Field(default=None, title="Country")
    description: str | None = Field(default=None, title="Description")
    locationCreated: Location | None = Field(default=None, title="Location Created")
    tags: list[IsolationTag] = Field(default_factory=list, title="Isolation Source Tags")
    source: list[SourceString] = Field(
        title="Source", description="List of JSON paths to source object"
    )
