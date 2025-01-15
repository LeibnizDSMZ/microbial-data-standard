from typing_extensions import Annotated
from pydantic import BaseModel, ConfigDict, Field, model_validator, StringConstraints

from microbial_strain_data_model.classes.enums import ColonyColor
from microbial_strain_data_model.classes.size import Size
from microbial_strain_data_model.utils.functions import check_not_completely_empty


class Colony(BaseModel):
    """Colony information of a microorganism/strain"""

    model_config = ConfigDict(
        strict=True,
        extra="forbid",
        revalidate_instances="always",
        str_strip_whitespace=True,
    )

    size: Size | None = Field(default=None, title="Size of Colony", alias="size")
    color: ColonyColor | None = Field(
        default=None, title="Color of Colony", alias="color"
    )
    source: Annotated[str, StringConstraints(pattern=r"^\/sources\/\d+$")] = Field(
        title="Source", alias="source", description="JSON path to source object"
    )

    _check_values = model_validator(mode="after")(check_not_completely_empty)
