# Программа: анализ введённой строки
# - сохраняет слова в кортеж
# - считает уникальные слова
# - считает гласные, согласные и знаки препинания

import string

# Получаем строку от пользователя
text = input("Введите строку слов, разделённых пробелами: ")

# Сохраняем слова в кортеж (split() по умолчанию разбивает по пробельным символам)
words = tuple(text.split())

# Количество уникальных слов (регистр не учитываем — приводим к нижнему)
unique_words = set(w.lower() for w in words)
print(f"\nКортеж слов: {words}")
print(f"Количество уникальных слов: {len(unique_words)}")

# Множества гласных и согласных (русские + английские)
vowels = set("аеёиоуыэюяaeiouy")
consonants = set("бвгджзйклмнпрстфхцчшщbcdfghjklmnpqrstvwxz")

# Знаки препинания — стандартный набор string.punctuation + русские
punctuation = set(string.punctuation + "«»…—–")

vowel_count = 0
consonant_count = 0
punct_count = 0

for ch in text.lower():
    if ch in vowels:
        vowel_count += 1
    elif ch in consonants:
        consonant_count += 1
    elif ch in punctuation:
        punct_count += 1

print(f"Количество гласных: {vowel_count}")
print(f"Количество согласных: {consonant_count}")
print(f"Количество знаков препинания: {punct_count}")