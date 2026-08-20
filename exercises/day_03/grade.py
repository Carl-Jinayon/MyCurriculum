grade = input("Enter grade (whole numbers): ")

if grade.isdigit():
    grade = int(grade)

    if 0 <= grade <= 100:
        if grade >= 90:
            print("Grade: A")
        elif grade >= 80:
            print("Grade: B")
        elif grade >= 70:
            print("Grade: C")
        elif grade >= 60:
            print("Grade: D")
        elif grade < 60:
            print("Grade: F")
        else:
            print("Error: Undefined input.")
    else:
        print("Invalid grade. Grade must be (0-100).")
else:
    print("Please enter a valid input.")