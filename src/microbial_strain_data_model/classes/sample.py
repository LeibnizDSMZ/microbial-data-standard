from typing_extensions import Annotated, Self
from pydantic import BaseModel, Field, StringConstraints, model_validator
from anytree.resolver import Resolver, ChildResolverError

from microbial_strain_data_model.data.isolation_sources_tree import root
from microbial_strain_data_model.classes.country import Country
from microbial_strain_data_model.classes.location import Location


class IsolationTag(BaseModel):
    level_1: str = Field(title="Level 1", alias="level1")
    level_2: str | None = Field(default=None, title="Level 2", alias="level2")
    level_3: str | None = Field(default=None, title="Level 3", alias="level3")

    @model_validator(mode="after")
    def check_isolation_tag(self) -> Self:
        resolver = Resolver("name")
        path = "" + self.level_1
        for x in [self.level_2, self.level_3]:
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
    country: Country | None = Field(default=None, title="Country", alias="country")
    description: str | None = Field(
        default=None, title="Description", alias="description"
    )
    location: Location | None = Field(
        default=None, title="Location Created", alias="locationCreated"
    )
    tags: list[IsolationTag] = Field(
        default_factory=list, title="Isolation Source Tags", alias="tags"
    )
    source: Annotated[str, StringConstraints(pattern=r"^\/sources\/\d+$")] = Field(
        title="Source", alias="source", description="JSON path to source object"
    )
