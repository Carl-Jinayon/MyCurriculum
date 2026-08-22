name = input("Enter your name: ")
age = int(input("Enter age: "))
height = float(input("Enter height: "))

print("\n---FULL DETAILS---")
print(f"Name: {name}, Age: {age}, Height: {height}m")

print("\n---Variable Types---")
print(f"Name Type  : {type(name)}")
print(f"Age Type   : {type(age)}")
print(f"Height Type: {type(height)}")