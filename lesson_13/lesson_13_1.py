from typing import Optional


class Human:

    def __init__(self, gender: str, age: int, first_name: str, last_name: str):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self) -> str:
        return f"Gender is {self.gender}, age is {self.age}, first_name is {self.first_name}, last_name is {self.last_name}"

class Student(Human):

    def __init__(self, gender: str, age: int, first_name: str, last_name: str, record_book: str):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self) -> str:
        return f"Gender is {self.gender}, age is {self.age}, first_name is {self.first_name}, last_name is {self.last_name}, record_book is {self.record_book}"

class GroupLimit(Exception):
    def __init__(self, group_number: str, max_size: int, text: Optional[str] = None):
        if text is None:
            self.text = f"Група {group_number} містить вже максимальну кількість студентів {max_size}"
        else:
            self.text = text
        super().__init__(self.text)

class Group:

    max_students = 10

    def __init__(self, number: str):
        self.number = number
        self.group = set()

    def add_student(self, student: Student) -> None:
        if len(self.group) >= self.max_students:
            raise GroupLimit(self.number, self.max_students)
        self.group.add(student)

    def delete_student(self, last_name: str) -> None:
        del_st = self.find_student(last_name)

        if del_st:
            self.group.discard(del_st)

    def find_student(self, last_name: str):
        for st in self.group:
            if st.last_name == last_name:
                return st
        return None

    def __str__(self) -> str:
        all_students = ""
        if not self.group:
            all_students = "No students in group"
        else:
            sorted_students = sorted(list(self.group), key=lambda s: (s.last_name, s.first_name))
            student_lines = [str(student) for student in sorted_students]
            all_students = "\n".join(student_lines)

        return f"Number:{self.number}\n{all_students}"

st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)
# print(gr)
assert str(gr.find_student('Jobs')) == str(st1), 'Test1'
assert gr.find_student('Jobs2') is None, 'Test2'
assert isinstance(gr.find_student('Jobs'), Student) is True, 'Метод поиска должен возвращать экземпляр'

gr.delete_student('Taylor')
print(gr)  # Only one student

gr.delete_student('Taylor')  # No error!
