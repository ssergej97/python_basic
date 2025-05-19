from typing import Optional, Set

from persons import Student

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