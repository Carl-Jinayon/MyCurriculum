import models
import reports
import storage

def main():
    data = storage.load_expenses()
    
    print("Welcome to expense tracker!")

    while True:
        print("\nMENU:"
            "\n1. Add expense"
            "\n2. List expenses"
            "\n3. Monthly summary"
            "\n4. Exit")

        try:
            choice = int(input("Enter choice: "))

            if choice == 1:
                try:
                    while True:
                        try:
                            amount = float(input("Enter amount: "))
                            try:
                                models.validate_amount(amount)
                            except ValueError as e:
                                print(e)
                            else:
                                break
                        except ValueError:
                            print("Invalid amount. Enter a number.")
                    while True:
                        try:
                            category = input("Enter category: ")
                            models.validate_category(category)
                        except ValueError as e:
                            print(e)
                        else:
                            break
                    while True:
                        try:
                            date = input("Enter date: ")
                            models.validate_date(date)
                        except ValueError:
                            print("Invalid date format. Use YYYY-MM-DD.")
                        else:
                            break
                    note = input("Enter note: ")
                except Exception as e:
                    print(f"Error: {e}")
                else:
                    models.create_expense(data, amount, category, date, note)
            elif choice == 2:
                print("\n1. List all" \
                      "\n2. Filter by category" \
                      "\n3. Filter by month" \
                      "\n4. Filter by category and month")

                try:
                    choice = int(input("Enter choice: "))

                    if choice == 1:
                        reports.list_expenses(data)
                    elif choice == 2:
                        while True:
                            try:
                                category = input("Enter category: ")
                                models.validate_category(category)
                            except ValueError as e:
                                print(e)
                            else:
                                filtered = reports.filter_by_category(data, category)
                                reports.list_expenses(filtered)
                                break
                    elif choice == 3:
                        while True:
                            try:
                                month = input("Enter month (YYYY-MM): ")
                                models.validate_month(month)
                            except ValueError as e:
                                print(e)
                            else:
                                filtered = reports.filter_by_month(data, month)
                                reports.list_expenses(filtered)
                                break
                    elif choice == 4:
                        while True:
                            try:
                                category = input("Enter category: ")
                                models.validate_category(category)
                            except ValueError as e:
                                print(e)
                            else:
                                break
                        while True:
                            try:
                                month = input("Enter month (YYYY-MM): ")
                                models.validate_month(month)
                            except ValueError as e:
                                print(e)
                            else:
                                filtered = reports.get_filtered_list(data, category, month)
                                reports.list_expenses(filtered)
                                break
                    else:
                        print("Invalid choice.")
                except ValueError:
                    print("Invalid choice.")
            elif choice == 3:
                try:
                    month = input("Enter month: ")
                    models.validate_month(month)
                except ValueError as e:
                    print(e)
                else:
                    reports.monthly_summary(data, month)
            elif choice == 4:
                print("Program exited with no errors.")
                break
            else:
                print("Invalid choice.")
        except ValueError:
            print("Invalid choice.")

if __name__ == "__main__":
    main()