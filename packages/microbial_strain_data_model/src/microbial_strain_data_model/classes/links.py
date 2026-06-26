# SPDX-FileCopyrightText: 2026 Leibniz Institute DSMZ-German Collection of Microorganisms and Cell Cultures GmbH
#
# SPDX-License-Identifier: MIT

from typing_extensions import Annotated

from pydantic import StringConstraints
from enum import Enum


SourceLink = Annotated[
    str,
    StringConstraints(pattern=r"^\/sources\/\d+$"),
]
RelationLink = Annotated[str, StringConstraints(pattern=r"^\/relatedData\/\d+$")]


class LinkType(str, Enum):
    source = "sources"
    related_data = "relatedData"
