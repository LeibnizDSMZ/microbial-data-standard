from typing_extensions import Annotated
from pydantic import BaseModel, Field, StringConstraints


class Application(BaseModel):
    """Application of the strain"""

    application: str = Field(title="Application", alias="application")
    source: Annotated[str, StringConstraints(pattern=r"^\/sources\/\d+$")] = Field(
        title="Source", alias="source", description="JSON path to source object"
    )
