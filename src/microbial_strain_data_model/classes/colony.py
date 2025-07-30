from pydantic import BaseModel, ConfigDict, Field, model_validator

from microbial_strain_data_model.classes.enums import ColonyColor
from microbial_strain_data_model.classes.size import Size
from microbial_strain_data_model.utils.functions import check_not_completely_empty

from microbial_strain_data_model.classes.links import SourceLink


class Colony(BaseModel):
    """Colony information of a microorganism/strain"""

    model_config = ConfigDict(
        strict=True,
        extra="forbid",
        revalidate_instances="always",
        str_strip_whitespace=True,
    )

    size: Size | None = Field(default=None, title="Size of Colony")
    color: ColonyColor | None = Field(
        default=None, title="Color of Colony", description="Color of the colony on the"
    )
    source: list[SourceLink] = Field(
        title="Source", description="List of JSON paths to source object"
    )

    _check_values = model_validator(mode="after")(check_not_completely_empty)
