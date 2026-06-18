# SPDX-FileCopyrightText: 2026 Leibniz Institute DSMZ-German Collection of Microorganisms and Cell Cultures GmbH
#
# SPDX-License-Identifier: MIT

from pathlib import Path
from microbial_strain_data_model.strain import Strain

_ROOT = Path(__file__).parent


def test_validate_bacteria_example() -> None:
    with _ROOT.joinpath("example_data/bacteria.json").open("r") as f_in:
        Strain.model_validate_json(f_in.read())


# def test_validate_fungi_example() -> None:
#    with _ROOT.joinpath("example_data/fungi.json").open("r") as f_in:
#        Strain.model_validate_json(f_in.read())
