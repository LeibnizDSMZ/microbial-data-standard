from pydantic import BaseModel, ConfigDict, Field

from microbial_strain_data_model.classes.enums import NagoyaRestrictions
from microbial_strain_data_model.classes.sourcestring import SourceLink
from microbial_strain_data_model.classes.country import Country


class Restriction(BaseModel):
    """Description"""

    model_config = ConfigDict(
        strict=True,
        extra="forbid",
        revalidate_instances="always",
        str_strip_whitespace=True,
    )

    name: str = Field(title="Name", description="Name of the restriction")
    country: Country | None = Field(default=None, title="Country")
    authority: str | None = Field(
        default=None, title="Authority", description="The responsible authority"
    )
    value: str = Field(title="Value")


class Legal(BaseModel):
    """Legal information of the strain"""

    model_config = ConfigDict(
        strict=True,
        extra="forbid",
        revalidate_instances="always",
        str_strip_whitespace=True,
    )

    dualUse: bool | None = Field(default=None, title="Dual Use")
    quarantineEU: bool | None = Field(default=None, title="Quarantine EU")
    nagoyaRestrictions: NagoyaRestrictions = Field(title="Nagoya Protocol Restrictions")
    qps: bool | None = Field(default=None, title="QPS")
    gras: bool | None = Field(default=None, title="GRAS")
    gmo: bool | None = Field(default=None, title="GMO")
    gmoInformation: str | None = Field(default=None, title="GMO Information")
    otherRestrictions: list[Restriction] = Field(
        default_factory=list, title="Other Restrictions"
    )
    source: list[SourceLink] = Field(
        title="Source", description="List of JSON paths to source object"
    )
