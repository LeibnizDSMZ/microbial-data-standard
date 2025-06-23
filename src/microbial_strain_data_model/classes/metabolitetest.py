from pydantic import BaseModel, ConfigDict, Field

from microbial_strain_data_model.classes.enums import MetaboliteTestType
from microbial_strain_data_model.classes.links import RelationLink


class MetaboliteTest(BaseModel):

    model_config = ConfigDict(
        strict=True,
        extra="forbid",
        revalidate_instances="always",
        str_strip_whitespace=True,
    )

    type: MetaboliteTestType = Field(title="Type")
    active: bool | None = Field(default=None, title="Active")
    protocol: str | None = Field(default=None, title="Protocol")
    kindOfUtilization: str | None = Field(default=None, title="Kind Of Utilization")
    relatedData: list[RelationLink] = Field(
        default_factory=list,
        title="Related Data",
        description="JSON paths to relation object",
    )
