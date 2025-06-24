import pytest

from string_utils import StringUtils

string_utils = StringUtils()

@pytest.mark.parametrize(
    "input_str,expected",
    [("hi", "Hi"), ("bye", "Bye"), ("hello", "Hello"),]
)
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.parametrize(
    "input_str,expected",
    [("999", "999"), ("0a", "0a"), ("  ", "  ")]
)
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.parametrize(
    "input_str,expected_output",
    [("  hello", "hello")]
)
def test_trim_positive(input_str, expected_output):
    result = string_utils.trim(input_str)
    assert result == expected_output


def test_trim_negative():
    string_utils = StringUtils()
    input_str = "Hello   "
    result = string_utils.trim(input_str)
    assert result == input_str


@pytest.mark.parametrize(
    'input_str, symbol, result',
    [("Test", "T", True), ("", "T", False), ("test", "T", False),
     ("Test", "P", False), ("Te1st", "1", True), ("Te st", " ", True),
     ("^^", "^", True)])
def test_contains(input_str, symbol, result):
    string = StringUtils()
    res = string.contains(input_str, symbol)
    assert res == result


@pytest.mark.parametrize(
    "input_str, symbol, result",
    [("NewYear", "New", "Year"), ("Home", "e", "Hom"), ("Hello", "l", "Heo")]
)
def test_delete_symbol_positive(input_str, symbol, result):
    string_utils = StringUtils()
    assert string_utils.delete_symbol(input_str, symbol) == result


@pytest.mark.parametrize(
    "input_str, symbol, expected_exception",
    [("Hello", None, TypeError)]
)
def test_delete_symbol_negative(input_str, symbol, expected_exception):
    string_utils = StringUtils()
    with pytest.raises(expected_exception):
        string_utils.delete_symbol(input_str, symbol)
