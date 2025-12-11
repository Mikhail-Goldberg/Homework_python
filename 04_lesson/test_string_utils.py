import pytest
from string_utils import StringUtils

string_utils = StringUtils()

@pytest.mark.positive
@pytest.mark.parametrize('word, result', [
    ('skypro', 'Skypro'),
    ('hello world', 'Hello world'),
    ('new-York', 'New-York'),
])
def test_capitalize_positive(word, result):
    string_utils = StringUtils()
    res = string_utils.capitalize(word)
    assert res == result

@pytest.mark.negative
@pytest.mark.parametrize('word, result',[
    ('12345ab', '12345ab'),
    ('', ''),
    (' ',' '),
])
def test_capitalize_negative(word, result):
    string_utils = StringUtils()
    res = string_utils.capitalize(word)
    assert res == result

@pytest.mark.positive
@pytest.mark.parametrize('word, result',[
    ('   skypro', 'skypro'),
    ('  1234', '1234'),
    (' !CITY', '!CITY'),
])
def test_trim_positive(word, result):
    string_utils = StringUtils()
    res = string_utils.trim(word)
    assert res == result

@pytest.mark.negative
@pytest.mark.parametrize('word, result',[
    ('Skypro', 'Skypro'),
    ('', ''),
    (' ', ''),
])
def test_trim_negative(word, result):
    string_utils = StringUtils()
    res = string_utils.trim(word)
    assert res == result

@pytest.mark.positive
@pytest.mark.parametrize('word, symbol, result',[
    ('Skypro', 'S', True),
    ('1234', '2', True),
    ('!CITY', '!', True),
])
def test_contains_positive(word, symbol, result):
    string_utils = StringUtils()
    res = string_utils.contains(word, symbol)
    assert res == result

@pytest.mark.negative
@pytest.mark.parametrize('word, symbol, result',[
    ('Skypro', 'u', False),
    ('1234', '5', False),
    ('', 'e', False),
])
def test_contains_negative(word, symbol, result):
    string_utils = StringUtils()
    res = string_utils.contains(word, symbol)
    assert res == result

@pytest.mark.positive
@pytest.mark.parametrize('word, symbol, result',[
    ('Skypro', 'S', 'kypro'),
    ('1234', '2', '134'),
    ('!CITY', '!', 'CITY'),
])
def test_delete_symbol_positive(word, symbol, result):
    string_utils = StringUtils()
    res = string_utils.delete_symbol(word, symbol)
    assert res == result

@pytest.mark.negative
@pytest.mark.parametrize('word, symbol, result',[
    ('Skypro', 'e', 'Skypro'),
    ('1234', '5', '1234'),
    (' ', ' ', ''),
])
def test_delete_symbol_negative(word, symbol, result):
    string_utils = StringUtils()
    res = string_utils.delete_symbol(word, symbol)
    assert res == result