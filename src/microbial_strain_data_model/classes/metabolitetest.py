from pydantic import BaseModel, Field

from microbial_strain_data_model.classes.enums import MetaboliteTestType


class MetaboliteTest(BaseModel):
    type: MetaboliteTestType = Field(title="Type", alias="type")
    active: bool | None = Field(default=None, title="Active", alias="active")
    protocol: str | None = Field(default=None, title="Protocol", alias="protocol")
    utilization: str | None = Field(
        default=None, title="Kind Of Utilization", alias="kindOfUtilization"
    )
