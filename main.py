def count_vowels(s):
    """
    Считает количество гласных в строке.
    Гласные: a, e, i, o, u (включая прописные и строчные буквы).
    """
    vowels = set("aeiouAEIOU")
    return sum(1 for char in s if char in vowels)