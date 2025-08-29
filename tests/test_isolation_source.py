import pytest
from microbial_strain_data_model.classes import isolationtag


def test_isolation_tag_system_1():
    assert isolationtag.IsolationTag(level1="#Environmental")


def test_isolation_tag_system_2():
    assert isolationtag.IsolationTag(level1="#Environmental", level2="#Terrestrial")


def test_isolation_tag_system_3():
    assert isolationtag.IsolationTag(
        level1="#Environmental", level2="#Terrestrial", level3="#Geologic"
    )


def test_no_data():
    with pytest.raises(ValueError, match=r".*"):
        isolationtag.IsolationTag()


def test_wrong_category_1():
    with pytest.raises(ValueError, match=r".*"):
        isolationtag.IsolationTag(
            level1="#StarWars", level2="#Terrestrial", level3="#Geologic"
        )


def test_wrong_category_2():
    with pytest.raises(ValueError, match=r".*"):
        isolationtag.IsolationTag(
            level1="#Environmental", level2="#StarWars", level3="#Geologic"
        )


def test_wrong_category_3():
    with pytest.raises(ValueError, match=r".*"):
        isolationtag.IsolationTag(
            level1="#Environmental", level2="#Terrestrial", level3="#StarWars"
        )
