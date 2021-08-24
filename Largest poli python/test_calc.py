import pytest
from calc import *


@pytest.fixture(scope='module')
def calc():
    calculators = {
        'good1': Calc(1),
        'good2': Calc(123),
        'good3': Calc(12321)
    }
    yield calculators


def test_make_list(calc):
    assert calc['good1']._make_list() == [1]
    assert calc['good2']._make_list() == [3, 2, 1]


def test_reverse(calc):
    assert calc['good1']._reverse_list() == [1]
    assert calc['good2']._reverse_list() == [1, 2, 3]

def test_is_poli(calc):
    assert calc['good1'].is_poli() is True
    assert calc['good2'].is_poli() is False
    assert calc['good3'].is_poli() is True

