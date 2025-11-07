import pytest
from src.luhn import luhnСheck


def test_good():
    assert luhnСheck("8571 2612 1234 5467")


def test_bad():
    assert not luhnСheck("4561 2612 1234 5463")


def test_short_numbers():
    assert not luhnCheck("1")
    assert not luhnCheck("12")


def test_valid_amex():
    assert luhnCheck("3782 822463 10005")


def test_valid_visa():
    assert luhnCheck("4111 1111 1111 1111")


def test_invalid_with_special_chars():
    assert not luhnCheck("4561-2612-1234-5463")
    assert not luhnCheck("4561 2612 1234 5463!")


def test_empty_string():
    assert not luhnCheck("")
    assert not luhnCheck("   ")


def test_only_non_digits():
    assert not luhnCheck("abcd efgh ijkl mnop")
