import pytest
@pytest.mark.podstawowe
def test_inny():
    assert 4 == 4

@pytest.mark.podstawowe
def test_true():
    assert True

@pytest.mark.szczegolowy
def test_czy_to_dziala():
    assert 1 == 2
