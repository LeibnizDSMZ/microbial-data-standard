# SPDX-FileCopyrightText: 2026 Leibniz Institute DSMZ-German Collection of Microorganisms and Cell Cultures GmbH
#
# SPDX-License-Identifier: MIT

from typing import Iterable
from microbial_strain_data_model.classes.source import Source
from microbial_strain_data_model.classes.links import LinkType
from microbial_strain_data_model.classes.relateddata import RelatedData


def build_link_mapping_and_merge[T: (Source, RelatedData)](
    left_link_list: list[T],
    right_link_list: list[T],
    link_type: LinkType,
) -> tuple[dict[str, str], Iterable[T]]:
    link: dict[str, str] = {}
    left_len = len(left_link_list)
    left_index = {obj.index(): ind for ind, obj in enumerate(left_link_list)}

    def _append_left_link() -> Iterable[T]:
        new_i = 0
        for right_index, right_link in enumerate(right_link_list):
            left_pos = left_index.get(right_link.index(), None)
            if left_pos is not None:
                link[f"/{link_type.value}/{right_index}"] = (
                    f"/{link_type.value}/{left_pos}"
                )
            else:
                link[f"/{link_type.value}/{right_index}"] = (
                    f"/{link_type.value}/{left_len + new_i}"
                )
                new_i += 1
                yield right_link

    return link, _append_left_link()
