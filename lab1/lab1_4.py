# -*- coding: utf-8 -*-

# Алфавиты для шифрования
RU_ALPHABET = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
EN_ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Словари для быстрого поиска
RU_LETTER_TO_NUM = {letter: i + 1 for i, letter in enumerate(RU_ALPHABET)}
EN_LETTER_TO_NUM = {letter: i + 1 for i, letter in enumerate(EN_ALPHABET)}

RU_NUM_TO_LETTER = {i + 1: letter for i, letter in enumerate(RU_ALPHABET)}
EN_NUM_TO_LETTER = {i + 1: letter for i, letter in enumerate(EN_ALPHABET)}


def encrypt(text: str, alphabet: str) -> str:
    """Преобразует текст в числовую последовательность (A1Z26)."""
    letter_to_num = RU_LETTER_TO_NUM if alphabet == "ru" else EN_LETTER_TO_NUM
    result = []
    for ch in text.upper():
        if ch in letter_to_num:
            result.append(str(letter_to_num[ch]))
        elif ch == " ":
            # пробел обозначаем нулём (разделитель слов)
            result.append("0")
        # остальные символы игнорируем
    return " ".join(result)


def decrypt(sequence: str, alphabet: str) -> str:
    """Преобразует числовую последовательность обратно в текст."""
    num_to_letter = RU_NUM_TO_LETTER if alphabet == "ru" else EN_NUM_TO_LETTER
    result = []
    # числа могут быть разделены пробелами, запятыми или дефисами
    tokens = sequence.replace(",", " ").replace("-", " ").split()
    for token in tokens:
        if not token.isdigit():
            raise ValueError(f"Некорректный элемент: '{token}'")
        num = int(token)
        if num == 0:
            result.append(" ")
        elif num in num_to_letter:
            result.append(num_to_letter[num])
        else:
            raise ValueError(f"Число {num} вне диапазона алфавита")
    return "".join(result)


def main():
    print("=== Шифр A1Z26 ===")
    print("1 — Зашифровать текст в числа")
    print("2 — Расшифровать числа в текст")
    choice = input("Выберите режим (1/2): ").strip()

    if choice not in ("1", "2"):
        print("Неверный выбор.")
        return

    lang = input("Язык алфавита (ru/en): ").strip().lower()
    if lang not in ("ru", "en"):
        print("Неверный язык.")
        return

    if choice == "1":
        text = input("Введите текст: ")
        try:
            encoded = encrypt(text, lang)
            print("Результат:", encoded)
        except Exception as e:
            print("Ошибка:", e)
    else:
        seq = input("Введите числовую последовательность (например: 16 18 10 3 6 20): ")
        try:
            decoded = decrypt(seq, lang)
            print("Результат:", decoded)
        except Exception as e:
            print("Ошибка:", e)


if __name__ == "__main__":
    main()