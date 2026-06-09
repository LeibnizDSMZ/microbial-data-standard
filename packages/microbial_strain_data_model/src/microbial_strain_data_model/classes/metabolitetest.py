from pydantic import BaseModel, ConfigDict, Field

from microbial_strain_data_model.classes.enums import (
    MetaboliteTestType,
    KindOfUtilization,
)
from microbial_strain_data_model.classes.links import RelationLink


class MetaboliteTest(BaseModel):
    model_config = ConfigDict(
        strict=True,
        extra="forbid",
        revalidate_instances="always",
        str_strip_whitespace=True,
    )

    type: MetaboliteTestType = Field(
        title="Type",
        description="The type of metabolic test, can be utilization or production",
    )
    active: bool | None = Field(
        default=None,
        title="Active",
        description="Is the metabolite utilization or production active",
    )
    protocol: str | None = Field(
        default=None, title="Protocol", description="What test was used"
    )
    kindOfUtilization: KindOfUtilization | None = Field(
        default=None,
        title="Kind Of Utilization",
        description="Only relevant if the type is utilization, "
        "as there are multiple kinds of utilization",
    )
    relatedData: list[RelationLink] = Field(
        default_factory=list,
        title="Related Data",
        description="JSON paths to relation object",
    )
