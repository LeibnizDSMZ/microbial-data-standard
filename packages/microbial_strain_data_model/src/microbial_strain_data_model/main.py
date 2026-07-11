# SPDX-FileCopyrightText: 2026 Leibniz Institute DSMZ-German Collection of Microorganisms and Cell Cultures GmbH
#
# SPDX-License-Identifier: MIT

from microbial_strain_data_model.strain import Strain


def run() -> None:
    print("strain", type(Strain))


if __name__ == "__main__":
    run()
