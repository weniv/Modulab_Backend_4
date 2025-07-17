import pytest
import calculator

@pytest.mark.it("1과 2의 합은 3이어야 합니다.")
def test_mysum_1():
    assert calculator.mysum(1, 2) == 3

@pytest.mark.it("100과 1000의 합은 1100이어야 합니다.")
def test_mysum_2():
    assert calculator.mysum(100, 1000) == 1100

@pytest.mark.it("10과 100의 합은 110이어야 합니다.")
def test_mysum_3():
    assert calculator.mysum(10, 100) == 110
