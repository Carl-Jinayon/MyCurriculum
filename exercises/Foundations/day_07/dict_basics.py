student = {
    "name": "Carl Jinayon",
    "age": 20,
    "gender": "Male",
    "graduated": False
}

print(f"Student name: {student["name"]}")

print(f"\nBefore age: {student.get("age")}")
student["age"] = 21
print(f"After age: {student.get("age")}")

student["course"] = "BSCoS"
print("\nAdded course key")
print(student)

print("\nBefore deleting a key:", student)
if student.get("graduated") is not None:
    del student["graduated"]
print("After deleting a key:", student)