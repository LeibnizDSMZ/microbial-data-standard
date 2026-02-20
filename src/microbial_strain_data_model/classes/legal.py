from pydantic import BaseModel, ConfigDict, Field, HttpUrl

from microbial_strain_data_model.classes.enums import NagoyaRestrictions
from microbial_strain_data_model.classes.links import SourceLink
from microbial_strain_data_model.classes.country import Country


class Restriction(BaseModel):
    """Restriction information."""

    model_config = ConfigDict(
        strict=True,
        extra="forbid",
        revalidate_instances="always",
        str_strip_whitespace=True,
    )

    name: str = Field(title="Name", description="Name of the restriction")
    country: Country | None = Field(
        default=None,
        title="Country",
        description="Country that put the restriction in place",
    )
    authority: str | None = Field(
        default=None, title="Authority", description="The responsible authority"
    )
    value: str = Field(title="Value", description="What is the restriction")
    url: HttpUrl | None = Field(
        default=None, title="URL", description="Link to the restriction documents"
    )


class Legal(BaseModel):
    """Legal information of the strain."""

    model_config = ConfigDict(
        strict=True,
        extra="forbid",
        revalidate_instances="always",
        str_strip_whitespace=True,
    )

    dualUse: bool | None = Field(default=None, title="Dual Use")
    quarantineEU: bool | None = Field(default=None, title="Quarantine EU")
    nagoyaRestrictions: NagoyaRestrictions = Field(
        title="Nagoya Protocol Restrictions",
        description="Are there any known Nagoya restrictions in place for this strain",
    )
    qps: bool | None = Field(
        default=None,
        title="QPS",
        description="Status of 'Qualified presumption of safety' by EFSA - "
        "European Union",
    )
    gras: bool | None = Field(
        default=None,
        title="GRAS",
        description="Status of 'Generally Recognized As Safe' by FDA - USA",
    )
    gmo: bool | None = Field(
        default=None, title="GMO", description="Is this strain genetically modified"
    )
    gmoInformation: str | None = Field(
        default=None, title="GMO Information", description="What was genetically modified"
    )
    otherRestrictions: list[Restriction] = Field(
        default_factory=list,
        title="Other Restrictions",
        description="List of restrictions in place for this strain",
    )
    source: list[SourceLink] = Field(
        title="Source", description="List of JSON paths to source object"
    )
