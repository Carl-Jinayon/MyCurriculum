class Student:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    def introduce(self):
        return f"I am {self.name}, {self.age} years old."

    def birthday(self):
        self.age += 1
        return self.age
