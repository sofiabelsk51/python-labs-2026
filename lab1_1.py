def is_uniq_number(seq):
    return len(seq) == len(set(seq))

data = input("Введите числа через пробел: ").split()
numbers = [int(n) for n in data]


if is_uniq_number(numbers):
    print("Все числа различны")
else:
    print("Есть повторяющиеся числа")