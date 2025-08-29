from pathlib import Path
from microbial_strain_data_model.strain import Strain


def test_validate_bacteria_example() -> None:
    with Path("./tests/example_data/bacteria.json").open("r") as f_in:
        Strain.model_validate_json(f_in.read())
