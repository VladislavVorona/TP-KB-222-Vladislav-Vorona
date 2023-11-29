import pytest
from lab_04 import CalcRPN

@pytest.fixture
def calc():
    return CalcRPN()

def test_NumCheck(calc):
    assert calc.NumCheck('5') == True
    assert calc.NumCheck('+') == False
    assert calc.NumCheck('Vladislave') == False

def test_OpPrior(calc):
    assert calc.OpPrior('+') == 0
    assert calc.OpPrior('-') == 0
    assert calc.OpPrior('*') == 1
    assert calc.OpPrior('/') == 1
    assert calc.OpPrior('^') == 2
    assert calc.OpPrior('%') == -1

def test_RPNGenerator(calc):
    assert calc.RPNGenerator('5 + 5') == ['5', '5', '+']
    assert calc.RPNGenerator('5 * ( 7 - 3 )') == ['5', '7', '3', '-', '*']
    assert calc.RPNGenerator('1 + 5 * 3') == ['1', '5', '3', '*', '+']

def test_CalculateRPN(calc):
    assert calc.CalculateRPN(['10', '5', '+']) == 15.0
    assert calc.CalculateRPN(['5', '7', '1', '-', '*']) == 30.0
    assert calc.CalculateRPN(['5', '2', '3', '*', '+']) == 11.0

if __name__ == '__main__':
    pytest.main()
