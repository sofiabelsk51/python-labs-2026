def get_valid_grade(course_name):
    # Получает и проверяет оценку по курсу
    while True:
        try:
            grade = int(input(f"  Введите оценку по курсу '{course_name}' (3-5): "))
            if 3 <= grade <= 5:
                return grade
            else:
                print("  ❌ Ошибка: оценка должна быть в диапазоне от 3 до 5 включительно!")
        except ValueError:
            print("  ❌ Ошибка: введите целое число!")


def get_valid_student_name():
    # Получает имя студента (не пустое)
    while True:
        name = input("Введите имя студента: ").strip()
        if name:
            return name
        print("  ❌ Ошибка: имя не может быть пустым!")


def main():
    # Названия курсов за последний успешно пройденный семестр
    courses = [
        "Программирование на Python",
        "Базы данных",
        "Алгоритмы и структуры данных",
        "Веб-разработка",
        "Компьютерные сети",
    ]

    print("=" * 50)
    print("Курсы за последний семестр:")
    for i, course in enumerate(courses, 1):
        print(f"  {i}. {course}")
    print("=" * 50)

    students = {}  # {имя: [оценки]}

    while True:
        print("\n--- Ввод данных студента ---")
        name = get_valid_student_name()

        grades = []
        for course in courses:
            grade = get_valid_grade(course)
            grades.append(grade)

        students[name] = grades

        cont = input("\nДобавить ещё студента? (y/n): ").strip().lower()
        if cont != "y":
            break

    if not students:
        print("Нет данных для анализа.")
        return

    # Сбор всех оценок
    all_grades = [g for grades in students.values() for g in grades]

    # Вывод результатов по каждому студенту
    print("\n" + "=" * 50)
    print("РЕЗУЛЬТАТЫ:")
    print("=" * 50)
    for name, grades in students.items():
        avg = sum(grades) / len(grades)
        print(f"\nСтудент: {name}")
        print(f"  Оценки: {grades}")
        print(f"  Средний балл: {avg:.2f}")

    # Общая статистика
    overall_avg = sum(all_grades) / len(all_grades)
    min_grade = min(all_grades)
    max_grade = max(all_grades)

    print("\n" + "=" * 50)
    print("ОБЩАЯ СТАТИСТИКА ПО ВСЕМ СТУДЕНТАМ:")
    print("=" * 50)
    print(f"  Количество студентов: {len(students)}")
    print(f"  Всего оценок: {len(all_grades)}")
    print(f"  Средний балл по всем студентам: {overall_avg:.2f}")
    print(f"  Минимальная оценка: {min_grade}")
    print(f"  Максимальная оценка: {max_grade}")


if __name__ == "__main__":
    main()