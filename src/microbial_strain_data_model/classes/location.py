from pydantic import BaseModel, ConfigDict, Field, model_validator
from pydantic_extra_types.coordinate import Latitude, Longitude

from microbial_strain_data_model.utils.functions import check_not_completely_empty


class GeoPoint(BaseModel):
    """Geopoint / Coordinate object"""

    model_config = ConfigDict(
        strict=True,
        extra="forbid",
        revalidate_instances="always",
        str_strip_whitespace=True,
    )

    latitude: Latitude = Field(title="Latitude", alias="latitude")
    longitude: Longitude = Field(title="Longitude", alias="longitude")
    elevation: float | None = Field(default=None, title="Elevation", alias="elevation")
    precision: float | None = Field(default=None, title="Precision", alias="precision")


class Location(BaseModel):
    """Location object"""

    model_config = ConfigDict(
        strict=True,
        extra="forbid",
        revalidate_instances="always",
        str_strip_whitespace=True,
    )

    name: str | None = Field(default=None, title="Name", alias="name")
    description: str | None = Field(
        default=None, title="Description", alias="description"
    )
    geo: GeoPoint | None = Field(default=None, title="Geo", alias="geo")

    _check_values = model_validator(mode="after")(check_not_completely_empty)
