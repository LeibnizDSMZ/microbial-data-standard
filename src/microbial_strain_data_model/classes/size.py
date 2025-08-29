from pydantic import BaseModel, ConfigDict, Field, PositiveFloat

from microbial_strain_data_model.classes.enums import SizeUnit


class Size(BaseModel):
    """size object, use only for micro and millimeter"""

    model_config = ConfigDict(
        strict=True,
        extra="forbid",
        revalidate_instances="always",
        str_strip_whitespace=True,
    )

    minimal: PositiveFloat = Field(title="Minimal")
    maximal: PositiveFloat = Field(title="Maximal")
    unit: SizeUnit = Field(title="Unit")
