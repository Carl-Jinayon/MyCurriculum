import storage
import reports
import models
import input_handler

def main():
    data = storage.load_expenses()

    print("Welcome to expense tracker!")

    MENU = [
        "Add expense",
        "List expenses",
        "Monthly summary",
        "Exit"
    ]
    while True:
        choice = input_handler.get_menu_choice(MENU)

        if choice == 1:
            amount = input_handler.get_amount()
            category = input_handler.get_category()
            date = input_handler.get_date()
            note = input_handler.get_note()

            models.create_expense(data, amount, category, date, note)
        elif choice  == 2:
            LIST_MENU = [
                "List all",
                "Filter by category",
                "Filter by month",
                "Filter by category and month"
            ]

            list_choice = input_handler.get_menu_choice(LIST_MENU)  

            if list_choice == 1:
                reports.list_expenses(data)
            elif list_choice == 2:
                category = input_handler.get_category()
                by_category = reports.filter_by_category(data, category)
                reports.list_expenses(by_category)
            elif list_choice == 3:
                month = input_handler.get_month()
                by_month = reports.filter_by_month(data, month)
                reports.list_expenses(by_month)
            elif list_choice == 4:
                category = input_handler.get_category()
                month = input_handler.get_month()
                by_category_month = reports.get_filtered_list(data, category, month)
                reports.list_expenses(by_category_month)
        elif choice == 3:
            month = input_handler.get_month()
            reports.monthly_summary(data, month)
        elif choice == 4:
            print("Program exited with no errors.")
            break
        
if __name__ == "__main__":
    main()