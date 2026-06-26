# SPDX-FileCopyrightText: 2026 Leibniz Institute DSMZ-German Collection of Microorganisms and Cell Cultures GmbH
#
# SPDX-License-Identifier: MIT

import pytest
from pathlib import Path
from microbial_strain_data_model.strain import Strain

_ROOT = Path(__file__).parent


@pytest.fixture
def fungi() -> None:
    # with ROOT.parent.joinpath("data/fungi.json").open("r") as f_in:
    #   Strain.model_validate_json(f_in.read())
    print("TODO")
    return None


@pytest.fixture
def fungi_min() -> Strain:
    with _ROOT.parent.joinpath("data/fungi_min.json").open("r") as f_in:
        return Strain.model_validate_json(f_in.read())
