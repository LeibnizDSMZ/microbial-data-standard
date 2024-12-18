from typing_extensions import Annotated
from pydantic import BaseModel, Field, StringConstraints

from microbial_strain_data_model.classes.enums import Host, PathogenLevel


class Pathogen(BaseModel):
    """Pathogen, defining Host, pathogenicity and under what classification"""

    host: Host = Field(title="Host", alias="host")
    pathogen: PathogenLevel = Field(title="Pathogen", alias="pathogen")
    classification: str | None = Field(
        default=None, title="Classification", alias="classification"
    )
    source: Annotated[str, StringConstraints(pattern=r"^\/sources\/\d+$")] = Field(
        title="Source", alias="source", description="JSON path to source object"
    )
