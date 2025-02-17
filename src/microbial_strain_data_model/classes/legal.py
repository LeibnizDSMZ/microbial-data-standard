from pydantic import BaseModel, ConfigDict, Field

from microbial_strain_data_model.classes.enums import NagoyaRestrictions
from microbial_strain_data_model.classes.sourcestring import SourceString


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
    source: list[SourceString] = Field(
        title="Source", description="List of JSON paths to source object"
    )
