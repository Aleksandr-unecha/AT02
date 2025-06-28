# AT02
 
# Счетчик гласных

Этот проект содержит функцию на Python для подсчета количества гласных в строке и набор тестов для проверки её корректности.

## Описание

Функция `count_vowels` принимает строку и возвращает количество гласных букв в ней. Гласными считаются буквы `a, e, i, o, u` в любом регистре.

## Установка

Для запуска проекта и тестов вам понадобится Python и библиотека `pytest`.

1. Установите Python с [официального сайта](https://www.python.org/downloads/).
2. Установите библиотеку `pytest` с помощью pip:

```bash
pip install pytest
```

## Запуск тестов

Для запуска тестов выполните следующую команду в терминале:
```bash
pytest test_main.py
```

## Примеры использования

Вот несколько примеров использования функции count_vowels:
```bash
print(count_vowels("aeiou"))  # Вывод: 5
print(count_vowels("AEIOU"))  # Вывод: 5
print(count_vowels("Hello World"))  # Вывод: 3
print(count_vowels("Python Programming"))  # Вывод: 4
print(count_vowels("AI and Machine Learning"))  # Вывод: 10
print(count_vowels("bcdfg"))  # Вывод: 0
print(count_vowels("12345"))  # Вывод: 0
print(count_vowels("!@#\$%"))  # Вывод: 0
print(count_vowels(""))  # Вывод: 0
```

## Структура проекта

- [main.py](main.py): Основной файл с функцией count_vowels.
- [test_main.py](test_main.py): Файл с тестами для функции count_vowels.
- [README.md](README.md): Файл с описанием проекта и инструкциями по установке и запуску.
