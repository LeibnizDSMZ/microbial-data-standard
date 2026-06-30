# SPDX-FileCopyrightText: 2026 Leibniz Institute DSMZ-German Collection of Microorganisms and Cell Cultures GmbH
#
# SPDX-License-Identifier: MIT

from typing import Callable


def to_string[T](
    to_cast: T | None, cast: Callable[[T], str] | None = None, /
) -> str | None:
    if to_cast is None:
        return None
    if cast is not None:
        return cast(to_cast)
    return str(to_cast)
