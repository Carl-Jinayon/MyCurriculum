username = input("Enter username: ")
password = input("Enter password: ")

if not username or not password:
    print("Please enter username or password.")
elif username == "admin" and password == "secret": 
    print("Access granted.")
else:
    print("Access denied.")