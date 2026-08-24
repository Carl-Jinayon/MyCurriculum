# Day 9 Advanced — Classes, Deeper

> STATUS: STRICTLY OPTIONAL (but this topic rewards curiosity). Never gates progress.

## 1. Advanced Technical Content

### Everything in Python is an object — even functions and types
```python
print(type(5))            # <class 'int'>   int is a CLASS
print(type("hi"))         # <class 'str'>
print(type(Student))      # <class 'type'>
print(type(s1))           # <class '__main__.Student'>
```
The ints, strings, dicts, sets you've used all along are instances of built-in CLASSES. `[].append()` is a method call. `"a".upper()` is a method call. You've been doing OOP since Day 1 without the label. Even classes are objects (of class `type`) — which is what makes Python so flexible.

### Dunder methods — teaching your objects to speak Python's native language
Methods with double underscores hook into Python's operators:
```python
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def __str__(self):                 # print(obj) → readable form
        return f"{self.owner}: ₱{self.balance}"

    def __repr__(self):                # developer form (debugger/repl)
        return f"BankAccount({self.owner!r}, {self.balance})"

    def __eq__(self, other):           # obj == obj2
        return (isinstance(other, BankAccount)
                and self.owner == other.owner
                and self.balance == other.balance)

    def __add__(self, other):          # obj + obj2
        return BankAccount(f"{self.owner}+{other.owner}",
                           self.balance + other.balance)
```
Implementing dunders = your objects integrate with `print`, `==`, `+`, `sorted`, `len` — instead of needing custom method names. This is why `sorted(dict.items())` "just works": tuples implemented comparison dunders.

### Class variables vs instance variables
```python
class Account:
    bank_name = "PyBank"               # CLASS variable — shared by all instances

    def __init__(self, owner):
        self.owner = owner             # INSTANCE variable — per object

a = Account("A"); b = Account("B")
a.bank_name == b.bank_name              # True — same shared value
Account.bank_name = "NewBank"           # changes it for EVERYONE
```
Rule of thumb: constants/shared config → class level; per-object data → instance level (`__init__`). Accidentally assigning `self.bank_name = ...` creates an instance shadow — a classic subtle bug.

### Properties — computed attributes that look like data
```python
class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    @property
    def fahrenheit(self):              # accessed WITHOUT parentheses
        return self.celsius * 9 / 5 + 32

t = Temperature(100)
t.fahrenheit                            # 212.0 — looks like an attribute!
```
Use when a value is derivable from others — callers never need to know.

### Composition over inheritance — the design principle that matters most
Beginners inherit everything; professionals compose:
```python
class Engine: ...
class Car:
    def __init__(self):
        self.engine = Engine()         # Car HAS-A Engine
```
Inherit only for genuine is-a relationships (Dog IS-A Animal; your error IS-A ValueError). Model has-a with attributes. This single judgment prevents most bad OOP designs you'd otherwise write in Stage 1–3.

### Exceptions with real payloads
```python
class ValidationError(ValueError):
    def __init__(self, field, message):
        self.field = field             # structured data, not just text
        super().__init__(f"{field}: {message}")

try:
    raise ValidationError("age", "must be positive")
except ValidationError as e:
    print(e.field)                     # caller can BRANCH on structured info
```
Text messages are for humans; attributes are for programs. Both, always.

## 2. Explore-It-Yourself Guide

1. `dir(5)` and `dir("hi")` — see the dunder machinery under every value.
2. Implement `__len__` on a class holding a list; then call `len(your_obj)`.
3. Make two instances equal by fields but different by identity (`is`) — explain both results.
4. Shadow experiment: set `a.bank_name = "hacked"` on one instance; check the other — unchanged? Now change at class level. Explain the difference.
5. Rewrite your Day 7 inventory dict as a class with dunders (`__str__`, `__len__`, `__getitem__`) until it feels like a native container.

## 3. Where This Leads Later
- Stage 1: full OOP design day — encapsulation, composition patterns, protocols/ABCs
- Dunder protocols → operator overloading, context managers (`__enter__/__exit__` — Day 8's `with`!), iterators
- Dataclasses (`@dataclass`) → boilerplate-free records for ML configs/datasets
- Exceptions with payloads → API error design (Stage 3), agent tool errors (Stage 4)

## Final Rule
Optional files never gate your progress — but for this topic, curiosity pays unusually well.