# SPDX-FileCopyrightText: 2026 Leibniz Institute DSMZ-German Collection of Microorganisms and Cell Cultures GmbH
#
# SPDX-License-Identifier: MIT

from microbial_strain_data_model.classes.links import LinkType
from typing import cast
from typing import TypeGuard
from copy import deepcopy
from typing import Mapping
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


def fix_source(root: _Source, map: Mapping[str, str | None], /) -> None:
    sources, hook = root._source()
    hook([mapped for src in sources if (mapped := map.get(src, src)) is not None])


def fix_related_data(root: _RelatedData, map: Mapping[str, str | None], /) -> None:
    for rel_data, hook in root._related_data():
        hook([mapped for rel in rel_data if (mapped := map.get(rel, rel)) is not None])


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


def _is_root(item: Root | _Source) -> TypeGuard[Root]:
    return hasattr(item, "_related_data")


def split_item[T: (Root, _Source)](
    to_split_ind: int,
    item: T,
    map_src: tuple[dict[str, str | None], dict[str, str | None]],
    map_rel: tuple[dict[str, str | None], dict[str, str | None]] | None = None,
    /,
) -> tuple[T | None, T | None]:
    to_split_src = f"/{LinkType.source.value}/{to_split_ind}"
    source_map_l, source_map_r = map_src
    copied: T | None = None
    is_root = map_rel is not None and _is_root(item)
    sources = tuple(item._source()[0])
    if to_split_src in sources:
        copied = deepcopy(item)
        fix_source(copied, source_map_r)
        if is_root:
            _, related_data_map_r = map_rel
            fix_related_data(cast(Root, copied), related_data_map_r)
    fix_source(item, source_map_l)

    if len(sources) == 0:
        return None, copied

    if is_root:
        related_data_map_l, _ = map_rel
        fix_related_data(item, related_data_map_l)

    return item, copied
