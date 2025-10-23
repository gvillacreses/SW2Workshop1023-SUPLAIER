class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name
        self.grades = []
        self.is_passed = False
        self.honor = "?"
    def add_grade(self, grade):
        if isinstance(grade, (int, float)):
            self.grades.append(grade)
        else:
            print("Invalid grade type. Must be numeric.")
    def calc_average(self):
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)
    def check_honor(self):
        avg = self.calc_average()
        if avg > 90:
            self.honor = "Yes"
        else:
            self.honor = "No"
    def delete_grade(self, index):
        if 0 <= index < len(self.grades):
            del self.grades[index]
        else:
            print("Invalid index. No grade deleted.")
    def report(self):
        print(f"ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Grades Count: {len(self.grades)}")
        print(f"Average: {self.calc_average():.2f}")
        print(f"Honor: {self.honor}")
        print(f"Passed: {'Yes' if self.is_passed else 'No'}")
def start_run():
    a = Student("x001", "Alice")
    a.add_grade(100)
    a.add_grade(80)
    a.calc_average()
    a.check_honor()
    a.delete_grade(1)
    a.report()
if __name__ == "__main__":
    start_run()