# Day 9 — Classes & OOP Primer: Objects, Methods, and Inheritance

## Objective
- Understand what a class is: a blueprint bundling data (attributes) and behavior (methods)
- Define classes with `__init__`, create instances, call methods
- Understand `self` — the instance a method operates on
- Use inheritance to create specialized classes (including custom exceptions, properly this time)
- Use `isinstance` for type checks
- Judge when a class is warranted vs plain functions + dicts

## Prerequisites
- Day 5: functions, parameters, return
- Day 7: dicts (the alternative to classes)
- Day 8: exceptions (being written alongside this lesson)

## Why This Matters
Day 8 asked you to write `class PositiveIntegerError(ValueError)` without explaining what a class *is* — a sequencing debt we're paying now. Classes are how real programs model things: accounts, users, expenses, network connections. More importantly, you cannot read professional Python (or any framework) without reading classes. This primer gives you the working minimum; full OOP design (polymorphism, composition patterns, dunder protocols) deepens in Stage 1.

## Mental Models

### 1. A Class Is a Blueprint; an Object Is a Building
The class defines what every instance will have (attributes = data) and can do (methods = behavior). You build the blueprint once; you pour concrete (instantiate) as many times as you want.

### 2. An Object Bundles Data WITH Its Operations
A dict can hold a student's data: `{"name": "Carl", "age": 20}`. But the *operations* on that data live somewhere else (loose functions). A class keeps them together:

```python
class Student:
    def __init__(self, name, age):
        self.name = name        # attribute
        self.age = age          # attribute

    def introduce(self):        # method
        return f"I am {self.name}, {self.age} years old."

s1 = Student("Carl", 20)       # instantiate — note: no 'self' here!
print(s1.introduce())          # I am Carl, 20 years old.
```

### 3. `self` = "this particular instance"
When you call `s1.introduce()`, Python secretly passes `s1` as `self`. Inside the method, `self.name` means "THIS student's name." That's why you define methods with `self` first but never pass it manually.

### 4. `__init__` Runs at Birth
`__init__(self, ...)` is the constructor — it runs automatically when you create an instance, setting up starting attributes.

## Inheritance — Building On What Exists

```python
class Animal:
    def __init__(self, name):
        self.name = name
    def speak(self):
        return "..."

class Dog(Animal):              # Dog IS-A Animal, extended
    def speak(self):
        return "Woof!"

a = Animal("Generic")
d = Dog("Rex")
d.name                          # "Rex"    — inherited attribute
d.speak()                       # "Woof!"  — overridden method
isinstance(d, Animal)           # True — a Dog IS an Animal
```

- `class Dog(Animal)` — Dog inherits everything from Animal
- Overriding: redefining `speak` replaces the inherited behavior
- `isinstance(obj, Class)` — asks "was this built from this class or its children?"

### The exception connection — finally explained:
```python
class PositiveIntegerError(ValueError):
    """Raised when input must be positive but isn't."""
    pass

try:
    raise PositiveIntegerError("got -3, need > 0")
except ValueError:              # CATCHES IT!
    print("caught as ValueError")
```
`PositiveIntegerError` inherits from `ValueError`, so `except ValueError` catches it too — inheritance means "is-a", and except matches is-a relationships. THAT is why your Day 8 exercise was shaped that way.

## When NOT to Use a Class (judgment)
Classes are not automatically better. Prefer plain functions + dicts when:
- You're just grouping a few values → dict is lighter
- Behavior is one transformation in → out → function
- No state needs protecting

Reach for a class when: multiple functions operate on the same data bundle AND that data has rules to enforce (validation at birth). Real judgment example coming in Project 1.

## Common Mistakes
- Forgetting `self` in method definitions (`def introduce():`) → TypeError on call
- Passing `self` manually (`s1.introduce(s1)`) → don't; Python does it
- Assigning attributes outside `__init__` inconsistently → instances with different shapes
- Confusing class (blueprint) with instance (building): `Student.introduce()` vs `s1.introduce()`
- Deep inheritance chains — keep it shallow; one level like exceptions is plenty at this stage

## Verification Checklist
- [ ] I can define a class with `__init__`, attributes, and methods
- [ ] I can instantiate and explain where `self` comes from
- [ ] I can subclass and override a method
- [ ] I can write a custom exception inheriting ValueError — and explain why except ValueError still catches it
- [ ] I can state one situation where a dict beats a class

## Exercises (exercises/Foundations/day_09/)
1. `student_class.py` — build the `Student` class above from memory; add a `birthday()` method that ages the student +1 and returns the new age.
2. `bank_account.py` — `BankAccount(owner, balance)` with `deposit(amount)` and `withdraw(amount)`. Withdraw must raise `InsufficientFundsError(needed, available)` — YOUR own exception class inheriting `ValueError`, carrying both numbers as attributes. Write the try/except demo proving it works.
3. `validator_oop.py` — build `get_positive_int(prompt)` that keeps asking until the user enters a positive integer, raising your `PositiveIntegerError(ValueError)` when the input is zero/negative before re-prompting, with a docstring explaining the contract (what it returns, what it raises). If you want a starting point, upgrade your own Day 5 `get_int()` from `validator_fn.py` — same loop skeleton, new exception behavior.
4. `shape_isinstance.py` — `Animal`/`Dog` hierarchy from the lesson; add `Cat`. Loop over `[Dog("Rex"), Cat("Mia"), Animal("?")]` printing each `.speak()` — polymorphism preview.
5. `class_vs_dict.py` — implement the same student record TWICE: once as dict + standalone function, once as class. In comments: which felt better and why? There's no wrong answer — the comparison IS the lesson.

## HARD MODE (optional, after core verified)
1. `account_str.py` — add `__str__(self)` to BankAccount so `print(account)` shows `BankAccount(Carl, ₱500)`; then add `__eq__` so two accounts with same owner+balance compare equal.
2. `savings.py` — `SavingsAccount(BankAccount)` adding `add_interest(rate)` (balance *= 1 + rate). Prove with isinstance: savings IS a bank account, and it still raises InsufficientFundsError correctly.
3. `inventory_class.py` — reimplement Day 7's inventory as a class: `Inventory(items_dict)` with `.sell(item, qty)`, `.restock(item, qty)`, `.total()`, `.most_stocked()` — wrapping your Day 7 logic behind methods.

## Mastery Check (from memory)
1. What runs automatically when you create an instance, and what is its first parameter?
2. Why does `except ValueError` catch `PositiveIntegerError`?
3. Write from memory: a `Temperature` class holding `celsius`, with `to_fahrenheit()` returning F.
4. One sentence: when would a dict be BETTER than a class?

## Reflection
- Did objects feel natural after dicts, or redundant? Where's the line for you?
- Which surprised you: inheritance mechanics or `self`?

## Key Takeaways
- Class = blueprint; instance = object built from it
- `__init__` sets up attributes; `self` = the particular instance
- Inheritance = is-a; overriding specializes; `except Parent` catches children
- Custom exceptions inherit ValueError — now you know WHY that works
- Dicts for passive data; classes when data + rules + operations belong together