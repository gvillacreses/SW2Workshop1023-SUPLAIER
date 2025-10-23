class Student:
    def __init__(self, student_id, name):
        if not student_id or not name:
            raise ValueError("Student ID and name cannot be empty.")
        self.student_id = student_id
        self.name = name
        self.grades = []
        self.average = 0
        self.letter_grade = "F"
        self.is_passed = False
        self.honor_roll = False

    def add_grade(self, grade):
        if isinstance(grade, (int, float)) and 0 <= grade <= 100:
            self.grades.append(grade)
        else:
            print("Invalid grade. Must be a number between 0 and 100.")

    def calc_average(self):
        if not self.grades:
            self.average = 0
        else:
            self.average = sum(self.grades) / len(self.grades)
        self._determine_letter_grade()
        self._determine_pass_fail()
        self._determine_honor_roll()

    def _determine_letter_grade(self):
        if self.average >= 90:
            self.letter_grade = "A"
        elif self.average >= 80:
            self.letter_grade = "B"
        elif self.average >= 70:
            self.letter_grade = "C"
        elif self.average >= 60:
            self.letter_grade = "D"
        else:
            self.letter_grade = "F"

    def _determine_pass_fail(self):
        self.is_passed = self.average >= 60

    def _determine_honor_roll(self):
        self.honor_roll = self.average >= 90

    def remove_grade_by_value(self, value):
        if value in self.grades:
            self.grades.remove(value)
        else:
            print("Grade value not found.")

    def remove_grade_by_index(self, index):
        if 0 <= index < len(self.grades):
            del self.grades[index]
        else:
            print("Invalid index. No grade deleted.")

    def generate_summary(self):
        self.calc_average()
        return (
            f"Student ID: {self.student_id}\n"
            f"Student Name: {self.name}\n"
            f"Number of Grades: {len(self.grades)}\n"
            f"Average Grade: {self.average:.2f}\n"
            f"Letter Grade: {self.letter_grade}\n"
            f"Pass/Fail: {'Passed' if self.is_passed else 'Failed'}\n"
            f"Honor Roll: {'Yes' if self.honor_roll else 'No'}\n"
        )

def start_run():
    a = Student("S001", "Alice")
    a.add_grade(95)
    a.add_grade(85)
    a.add_grade(70)
    print(a.generate_summary())
    a.remove_grade_by_index(1)
    a.remove_grade_by_value(70)
    print(a.generate_summary())

if __name__ == "__main__":
    start_run()
