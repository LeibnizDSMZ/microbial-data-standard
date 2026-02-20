from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    HttpUrl,
    model_validator,
)

from microbial_strain_data_model.utils.functions import check_not_completely_empty
from microbial_strain_data_model.classes.links import SourceLink


class OtherMedia(BaseModel):
    """A Media object e.g. Photo, Video, Document, etc."""

    model_config = ConfigDict(
        strict=True,
        extra="forbid",
        revalidate_instances="always",
        str_strip_whitespace=True,
    )

    url: HttpUrl | None = Field(default=None, title="URL", description="Link to medium")
    name: str | None = Field(default=None, title="Name")
    description: str | None = Field(
        default=None,
        title="Description",
        description="Description of the medium and the content in the medium",
    )
    usageInfo: str | None = Field(
        default=None,
        title="Usage Information",
        description="License or other information on usage",
    )
    additionalType: str | None = Field(default=None, title="Additional Type")
    source: list[SourceLink] = Field(
        title="Source", description="List of JSON paths to source object"
    )

    _check_values = model_validator(mode="after")(check_not_completely_empty)
