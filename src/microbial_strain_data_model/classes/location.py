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

    latitude: Latitude = Field(
        title="Latitude", description="Should be a float value between -90 and 90"
    )
    longitude: Longitude = Field(
        title="Longitude", description="Should be a float value between -180 and 180"
    )
    elevation: float | None = Field(default=None, title="Elevation")
    precision: float | None = Field(default=None, title="Precision")


class Location(BaseModel):
    """Location object"""

    model_config = ConfigDict(
        strict=True,
        extra="forbid",
        revalidate_instances="always",
        str_strip_whitespace=True,
    )

    name: str | None = Field(
        default=None, title="Name", description="Name of the location, e.g. 'Lake Como'"
    )
    description: str | None = Field(
        default=None, title="Description", description="Description of the location"
    )
    geo: GeoPoint | None = Field(
        default=None, title="Geo", description="Precise location coordinates"
    )

    _check_values = model_validator(mode="after")(check_not_completely_empty)
