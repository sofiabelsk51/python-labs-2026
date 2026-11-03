import math

def find_third_side():
    print("Нахождение третьей стороны прямоугольного треугольника")
    print("Что известно?")
    print("1 - Два катета (найти гипотенузу)")
    print("2 - Катет и гипотенуза (найти второй катет)")
    
    choice = input("Выберите вариант (1 или 2): ").strip()
    
    try:
        if choice == "1":
            a = float(input("Введите первый катет: "))
            b = float(input("Введите второй катет: "))
            
            if a <= 0 or b <= 0:
                print("Стороны должны быть положительными числами!")
                return
            
            c = math.sqrt(a**2 + b**2)
            print(f"Гипотенуза = {c:.4f}")
            
        elif choice == "2":
            a = float(input("Введите катет: "))
            c = float(input("Введите гипотенузу: "))
            
            if a <= 0 or c <= 0:
                print("Стороны должны быть положительными числами!")
                return
            
            if c <= a:
                print("Ошибка: гипотенуза должна быть больше катета!")
                return
            
            b = math.sqrt(c**2 - a**2)
            print(f"Второй катет = {b:.4f}")
            
        else:
            print("Неверный выбор. Введите 1 или 2.")
            
    except ValueError:
        print("Ошибка: введите корректное число!")


if __name__ == "__main__":
    find_third_side()