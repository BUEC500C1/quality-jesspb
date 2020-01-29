from hw1 import getRoman


def test_1():
    assert getRoman(1014) == 'MXIV'


def test_2():
    assert getRoman(6) == 'VI'


def test_3():
    assert getRoman(1776) == 'MDCCLXXVI'
