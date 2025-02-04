from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    HttpUrl,
    model_validator,
)

from microbial_strain_data_model.utils.functions import check_not_completely_empty
from microbial_strain_data_model.classes.sourcestring import SourceString


class OtherMedia(BaseModel):
    """A Media object e.g. Photo, Video, Document, etc"""

    model_config = ConfigDict(
        strict=True,
        extra="forbid",
        revalidate_instances="always",
        str_strip_whitespace=True,
    )

    url: HttpUrl | None = Field(default=None, title="URL", alias="url")
    name: str | None = Field(default=None, title="Name", alias="name")
    description: str | None = Field(
        default=None, title="Description", alias="description"
    )
    usage: str | None = Field(default=None, title="Usage Information", alias="usageInfo")
    additional_type: str | None = Field(
        default=None, title="Additional Type", alias="additionalType"
    )
    source: list[SourceString] = Field(
        title="Source", alias="source", description="List of JSON paths to source object"
    )

    _check_values = model_validator(mode="after")(check_not_completely_empty)
