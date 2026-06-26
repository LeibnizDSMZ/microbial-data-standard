# SPDX-FileCopyrightText: 2026 Leibniz Institute DSMZ-German Collection of Microorganisms and Cell Cultures GmbH
#
# SPDX-License-Identifier: MIT

from typing import Protocol
from typing import Callable
from typing import Iterable

type ROOT_HOOK = tuple[Iterable[str], Callable[[list[str]], None]]


class _Source(Protocol):
    def _source(self) -> ROOT_HOOK: ...


class _RelatedData(Protocol):
    def _related_data(self) -> Iterable[ROOT_HOOK]: ...


class Root(Protocol):
    def _source(self) -> ROOT_HOOK: ...
    def _related_data(self) -> Iterable[ROOT_HOOK]: ...


def fix_source(root: _Source, map: dict[str, str], /) -> None:
    sources, hook = root._source()
    hook([map[src] for src in sources])


def fix_related_data(root: _RelatedData, map: dict[str, str], /) -> None:
    for rel_data, hook in root._related_data():
        hook([map[rel] for rel in rel_data])


def _join_related_data(origin: Root, to_join: Root, /) -> None:
    for ele_cur, ele_join in zip(origin._related_data(), to_join._related_data()):
        rel_data, hook = ele_cur
        new_rel = set(rel_data)
        new_rel.update(ele_join[0])
        hook(list(new_rel))


def _join_source(origin: Root, to_join: Root, /) -> None:
    sources, hook = origin._source()
    new_src = set(sources)
    new_src.update(to_join._source()[0])
    hook(list(new_src))


def join_links(origin: Root, to_join: Root, /) -> None:
    _join_source(origin, to_join)
    _join_related_data(origin, to_join)
