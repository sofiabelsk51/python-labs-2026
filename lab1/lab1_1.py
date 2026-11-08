def is_uniq_number(seq):
    return len(seq) == len(set(seq))

data = input("Введите числа через пробел: ").split()

if is_uniq_number(data):
    print("Все числа различны")
else:
    print("Есть повторяющиеся числа")