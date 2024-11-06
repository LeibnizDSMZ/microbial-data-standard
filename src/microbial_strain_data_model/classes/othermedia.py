from typing_extensions import Annotated
from pydantic import BaseModel, Field, HttpUrl, model_validator, StringConstraints

from microbial_strain_data_model.utils.functions import check_not_completely_empty


class OtherMedia(BaseModel):
    """A Media object e.g. Photo, Video, Document, etc"""

    url: HttpUrl | None = Field(default=None, title="URL", alias="url")
    name: str | None = Field(default=None, title="Name", alias="name")
    description: str | None = Field(
        default=None, title="Description", alias="description"
    )
    usage: str | None = Field(default=None, title="Usage Information", alias="usageInfo")
    additional_type: str | None = Field(
        default=None, title="Additional Type", alias="additionalType"
    )
    source: Annotated[str, StringConstraints(pattern=r"^\/sources\/\d+$")] = Field(
        title="Source", alias="source", description="JSON path to source object"
    )

    _check_values = model_validator(mode="after")(check_not_completely_empty)
