from typing_extensions import Annotated
from pydantic import BaseModel, ConfigDict, Field, StringConstraints


class Application(BaseModel):
    """Application of the strain"""

    model_config = ConfigDict(
        strict=True,
        extra="forbid",
        revalidate_instances="always",
        str_strip_whitespace=True,
    )

    application: str = Field(title="Application", alias="application")
    source: Annotated[str, StringConstraints(pattern=r"^\/sources\/\d+$")] = Field(
        title="Source", alias="source", description="JSON path to source object"
    )
