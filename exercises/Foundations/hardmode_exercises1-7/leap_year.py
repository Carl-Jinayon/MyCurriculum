try:
    year = int(input("Enter year: "))
except ValueError:
    print("Please enter valid input.")
else:
    if year % 4 == 0 and (year - (year % 100)) % 400 == 0:
            print("leap")
    else:
        print("not")
