from typing_extensions import Annotated

from pydantic import StringConstraints


SourceLink = Annotated[
    str,
    StringConstraints(pattern=r"^\/sources\/\d+$"),
]
RelationLink = Annotated[str, StringConstraints(pattern=r"^\/relatedData\/\d+$")]
