# SPDX-FileCopyrightText: 2026 Leibniz Institute DSMZ-German Collection of Microorganisms and Cell Cultures GmbH
#
# SPDX-License-Identifier: MIT

import pytest
from pathlib import Path
from microbial_strain_data_model.strain import Strain

_ROOT = Path(__file__).parent


@pytest.fixture
def micro_left() -> Strain:
    with _ROOT.parent.joinpath("data/merge_a.json").open("r") as f_in:
        return Strain.model_validate_json(f_in.read())


@pytest.fixture
def micro_right() -> Strain:
    with _ROOT.parent.joinpath("data/merge_b.json").open("r") as f_in:
        return Strain.model_validate_json(f_in.read())
