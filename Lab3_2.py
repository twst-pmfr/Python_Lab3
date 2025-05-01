class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"{self.name}, {self.age} years old"

# Дочерний класс Teacher от базового класса Person
class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age)  # наследуем имя и возраст от родительского класса
        self.subject = subject  # предмет преподавателя
        self.students = []  # список учеников изначально пустой

    # метод добавления студента
    def add_student(self, student):
        if isinstance(student, Student):  # проверяем тип объекта перед добавлением
            self.students.append(student)

    # метод удаления студента
    def remove_student(self, student_name):
        for s in self.students:
            if s.name == student_name:
                self.students.remove(s)
                break
        else:
            print(f"Студент с именем '{student_name}' не найден.")

    # метод вывода списка всех студентов учителя
    def list_students(self):
        if not self.students:
            print("У вас пока нет студентов.")
        else:
            print(f"Список студентов у {self.name}:")
            for student in self.students:
                print(f"- {student.introduce()}")

            # Класс Student также наследуется от Person


class Student(Person):
    def __init__(self, name, age):
        super().__init__(name, age)

# Создаем объекты преподавателей и студентов
teacher_math = Teacher('Иван Петров', 45, 'Математика')
student_anna = Student('Анна Иванова', 17)
student_pavel = Student('Павел Сидоров', 18)

# Добавляем студентов учителю математики
teacher_math.add_student(student_anna)
teacher_math.add_student(student_pavel)

# Список студентов
teacher_math.list_students()

# Удаление одного студента
teacher_math.remove_student('Анна Иванова')

# Проверка обновленного списка
teacher_math.list_students()