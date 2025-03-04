import pytest
from main import count_vowels

def test_only_vowels():
    """
    Проверяет, что функция правильно считает гласные в строке,
    содержащей только гласные.
    """
    assert count_vowels("aeiou") == 5
    assert count_vowels("AEIOU") == 5
    assert count_vowels("aEiOu") == 5

def test_no_vowels():
    """
    Проверяет, что функция возвращает 0 для строки,
    не содержащей гласных.
    """
    assert count_vowels("bcdfg") == 0
    assert count_vowels("12345") == 0
    assert count_vowels("!@#$%") == 0
    assert count_vowels("") == 0

def test_mixed_strings():
    """
    Проверяет, что функция правильно считает гласные
    в смешанных строках (включая прописные и строчные буквы).
    """
    assert count_vowels("Hello World") == 3  # e, o, o
    assert count_vowels("Python Programming") == 4  # o, o, a, i
    assert count_vowels("AI and Machine Learning") == 10  # A, I, a, i, e, a, i, e, i, o

def test_empty_string():
    """
    Проверяет, что функция корректно обрабатывает пустую строку.
    """
    assert count_vowels("") == 0