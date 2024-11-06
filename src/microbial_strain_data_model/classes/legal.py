from typing_extensions import Annotated
from pydantic import BaseModel, Field, StringConstraints

from microbial_strain_data_model.classes.enums import NagoyaRestrictions


class Legal(BaseModel):
    """Legal information of the strain"""

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
    source: Annotated[str, StringConstraints(pattern=r"^\/sources\/\d+$")] = Field(
        title="Source", alias="source", description="JSON path to source object"
    )
