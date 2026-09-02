class InvalidAmountError(ValueError):
    """Raised when amount is not a valid positive number."""
    def __init__(self):
        super().__init__("Amount must be a positive number.")

class InvalidDateError(ValueError):
    """Raised when date is invalid or wrong format."""
    def __init__(self):
        super().__init__("Invalid date. Use YYYY-MM-DD.")

class InvalidCategoryError(ValueError):
    """Raised when category is not in the allowed list."""
    def __init__(self):
        super().__init__("Invalid category. Choose: food, transport, rent, utilities, other")

class InvalidMonthError(ValueError):
    """Raised when month format is invalid."""
    def __init__(self):
        super().__init__("Invalid month. Use YYYY-MM.")
