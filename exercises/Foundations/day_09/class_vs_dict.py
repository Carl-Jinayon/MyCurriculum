# ==========================================
# 1. Student record using a dictionary
# ==========================================

student_dict = {
    "name": "Carl Jinayon",
    "age": 20,
    "grade": 95
}


def display_student(student):
    print(f"Name: {student['name']}")
    print(f"Age: {student['age']}")
    print(f"Grade: {student['grade']}")


print("Dictionary version:")
display_student(student_dict)

# ==========================================
# 2. Student record using a class
# ==========================================

class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Grade: {self.grade}")


student_class = Student("Carl Jinayon", 20, 95)

print("\nClass version:")
student_class.display()


# ==========================================
# Comparison
# ==========================================

# I preferred the class-based approach because the data and the
# behavior are grouped together. The dictionary approach is simpler
# for a basic record, but the class feels more organized when the
# student has multiple behaviors or methods.
