class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = []

    # Добавляет оценку с проверкой диапазона
    def add_grade(self, grade):
        if not isinstance(grade, (int, float)) or grade < 0 or grade > 10:
            raise ValueError("Оценка должна быть числом от 0 до 10")
        self.grades.append(grade)

    # Возвращает среднее арифметическое всех оценок
    def get_average(self):
        return sum(self.grades) / len(self.grades) if self.grades else None

    # Красивое отображение информации о студенте
    def display_info(self):
        print(f'Имя студента: {self.name}')
        print(f'ID студента: {self.student_id}')
        print(f'Средний балл: {self.get_average():.2f}' if self.grades else 'Нет оценок')

    # Строковое представление объекта
    def __str__(self):
        avg = f'{self.get_average():.2f}' if self.grades else 'нет'
        return f'Student(name={self.name}, id={self.student_id}, average={avg})'

    # Сравнение объектов по идентификатору
    def __eq__(self, other):
        if isinstance(other, Student):
            return self.student_id == other.student_id
        return False

    # Длина — количество оценок
    def __len__(self):
        return len(self.grades)

# Создаем объект студента
sasha = Student('Александр', 'S12345')

# Проверяем строку представления
print(sasha.__str__())  # Output: Student(name=Александр, id=S12345, average=нет)

# Добавляем оценки
sasha.add_grade(8)
sasha.add_grade(7)
sasha.add_grade(9)

# Получаем среднюю оценку
average = sasha.get_average()
print(f"Средняя оценка Александра: {average:.2f}")  # Output: Средняя оценка Александра: 8.00

# Красиво выводим информацию
sasha.display_info()

# Количество оценок
print(len(sasha))  # Output: 3

# Создание другого объекта студента
masha = Student('Мария', 'S12345')  # тот же ID

# Проверка равенства студентов по идентификатору
if sasha == masha:
    print("Студенты совпадают по идентификатору")  # Output: Студенты совпадают по идентификатору
else:
    print("Разные студенты")