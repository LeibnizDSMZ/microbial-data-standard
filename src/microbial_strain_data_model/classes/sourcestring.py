from typing_extensions import Annotated

from pydantic import StringConstraints


SourceString = Annotated[str, StringConstraints(pattern=r"^\/sources\/\d+$")]
