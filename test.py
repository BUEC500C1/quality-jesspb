from hw1 import getRoman


def test_1():
    assert getRoman(1014) == 'MXIV'


def test_2():
    assert getRoman(6) == 'VI'


def test_3():
    assert getRoman(1776) == 'MDCCLXXVI'


def test_string():
    assert getRoman('invalid') == ''


def test_decimal():
    assert getRoman(1.776) == ''


def test_mix():
    assert getRoman('1776invalid') == ''
