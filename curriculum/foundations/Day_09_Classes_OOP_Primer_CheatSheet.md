# Day 9 Cheat Sheet — Classes & OOP Primer

## Blueprint syntax
```python
class Student:
    def __init__(self, name, age):   # constructor — runs at birth
        self.name = name             # attribute
        self.age = age

    def introduce(self):             # method (self = this instance)
        return f"{self.name}, {self.age}"

s = Student("Carl", 20)   # instantiate — don't pass self!
s.introduce()             # Python passed s as self automatically
s.name                    # attribute access
```

## Inheritance
```python
class Dog(Animal):        # Dog IS-A Animal
    def speak(self):      # overrides Animal.speak
        return "Woof!"

isinstance(d, Animal)     # True
```

## Exceptions inherit — that's the trick
```python
class MyError(ValueError):
    pass

try: raise MyError("bad")
except ValueError:        # CATCHES it — is-a relationship
    ...
# carry data: super().__init__(msg); self.code = code
```

## None-checking on objects
```python
if result is None: ...
isinstance(x, SomeClass)
```

## Class vs Dict judgment
| Use dict | Use class |
|---|---|
| passive data bundle | data + rules + operations together |
| one-off transformation | state enforced at birth, multiple methods |

## Common Errors
- forgot `self` in def → TypeError on call
- `Class.method()` instead of instance call
- attributes created inconsistently outside __init__
- deep inheritance chains → keep shallow

## Must-Know Checklist
- [ ] define class + __init__ + method from memory
- [ ] explain self's origin
- [ ] subclass + override
- [ ] custom exception inheriting ValueError + explain catch behavior
- [ ] dict-vs-class judgment sentence

## Active Recall
1. What runs automatically at instance creation? First parameter?
2. Why does except ValueError catch PositiveIntegerError?
3. Temperature class with celsius + to_fahrenheit() — write from memory.
4. When does a dict beat a class?