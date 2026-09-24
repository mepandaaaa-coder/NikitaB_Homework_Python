import pytest
from string_utils import StringUtils

string_utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("test", "Test"),
    ("hello world", "Hello world"),
    ("pyton", "Pyton"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("", ""),
    ("  ", "  "),
    ("123", "123"),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("  skypro", "skypro"),
    ("hello world", "hello world"),
    ("  ", ""),
])
def test_trim_positive(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("", ""),
    ("  text ", "text "),
])
def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("Skypro", "S", True),
    ("hello world", "o", True),
    ("123", "1", True),
])
def test_contains_positive(input_str, symbol, expected):
    assert string_utils.contains(input_str, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("Skypro", "U", False),
    ("", "a", False),
    ("123", "b", False),
])
def test_contains_negative(input_str, symbol, expected):
    assert string_utils.contains(input_str, symbol) == expected


@pytest.mark.positive
@pytest.mark.parametrize("string, symbol, exepted", [
    ("Skypro", "k", "Sypro"),
    ("Skypro", "pro", "Sky"),
    ("123", "3", "12"),
])
def test_delete_symbol_positive(string, symbol, exepted):
    assert string_utils.delete_symbol(string, symbol) == exepted


@pytest.mark.negative
@pytest.mark.parametrize("string, symbol, exepted", [
    ("", "a", ""),
    ("hello", "z", "hello"),
    ("  ", " ", ""),
])
def test_delete_symbol_negative(string, symbol, exepted):
    assert string_utils.delete_symbol(string, symbol) == exepted
