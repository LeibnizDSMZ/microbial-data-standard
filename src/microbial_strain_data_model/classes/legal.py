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

    dual_use: bool | None = Field(default=None, title="Dual Use", alias="dualUse")
    quarantine: bool | None = Field(
        default=None, title="Quarantine EU", alias="quarantineEU"
    )
    nagoya: NagoyaRestrictions = Field(
        title="Nagoya Protocol Restrictions", alias="nagoyaRestrictions"
    )
    QPS: bool | None = Field(default=None, title="QPS", alias="qps")
    GRAS: bool | None = Field(default=None, title="GRAS", alias="gras")
    gmo: bool | None = Field(default=None, title="GMO", alias="gmo")
    gmo_information: str | None = Field(
        default=None, title="GMO Information", alias="gmoInformation"
    )
    source: list[SourceString] = Field(
        title="Source", alias="source", description="List of JSON paths to source object"
    )
