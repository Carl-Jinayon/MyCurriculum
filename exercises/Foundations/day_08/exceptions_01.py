def safe_int(s):
    """Returns integer value of s. If conversion fails, it returns None."""
    try:
        s = int(s)
        # Can use int(float(s)) - if the program should also handle floating point numbers.
    except ValueError:
        return None
    else:
        return s

print(safe_int("42")) # prints 42
print(safe_int("3.14")) # prints None
print(safe_int("hello")) # prints None