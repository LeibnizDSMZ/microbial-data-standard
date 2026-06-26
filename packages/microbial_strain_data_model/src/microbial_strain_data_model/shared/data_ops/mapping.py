# SPDX-FileCopyrightText: 2026 Leibniz Institute DSMZ-German Collection of Microorganisms and Cell Cultures GmbH
#
# SPDX-License-Identifier: MIT

from typing import Any
from typing import Iterable
from microbial_strain_data_model.classes.source import Source
from microbial_strain_data_model.classes.links import LinkType
from microbial_strain_data_model.classes.relateddata import RelatedData


def _append_link[T: (Source, RelatedData)](
    map: dict[str, str],
    core_index: dict[tuple[Any, ...], int],
    link_con: list[T],
    link_type: LinkType,
    /,
) -> Iterable[T]:
    new_i = 0
    ori_len = len(core_index)
    for old_ind, to_link in enumerate(link_con):
        key = to_link.index()
        uni_pos = core_index.get(key, None)
        if uni_pos is not None:
            map[f"/{link_type.value}/{old_ind}"] = f"/{link_type.value}/{uni_pos}"
        else:
            new_pos = ori_len + new_i
            map[f"/{link_type.value}/{old_ind}"] = f"/{link_type.value}/{new_pos}"
            core_index[key] = new_pos
            yield to_link
            new_i += 1


def build_link_mapping_and_merge[T: (Source, RelatedData)](
    left_link_list: list[T],
    right_link_list: list[T],
    link_type: LinkType,
) -> tuple[dict[str, str], dict[str, str], list[T]]:
    link_left: dict[str, str] = {}
    link_right: dict[str, str] = {}
    core_index = {}
    merged = [
        *_append_link(link_left, core_index, left_link_list, link_type),
        *_append_link(link_right, core_index, right_link_list, link_type),
    ]
    return (link_left, link_right, merged)
