#Expense Tracker App

def main():
    hello()
    expenses = []
    while True:
        display_menu()
        action = get_action_number()
        match action:
            case "1":
                add_expense(expenses)
            case "2":
                view_expenses(expenses)
            case "3":
                total_spent(expenses)
            case "4":
                category_breakdown(expenses)
            case "5":
                print("Have a nice day, Good-bye")
                break

def hello():
    print("Welcome in expense tracker app.")

def display_menu():
    print("1. Add expense \n2. View expenses \n3. Total spent"
        + "\n4. Category breakdown \n5. Exit")

def get_action_number():
    while True:
        action = input("Choose action number: ")
        match action:
            case "1" | "2" | "3" | "4" | "5":
                return action
            case _:
                print("Enter a valid action number")

def add_expense(expenses):
    while True:
        try:
            amount = float(input("Enter expense amount: "))
        except ValueError:
            print("Just (Float/Integer - Positive) numbers is allowed.")
        else:
            if amount <= 0:
                print("Just (Float/Integer - Positive) numbers is allowed.")
                continue

            while True:
                category = input("Enter expense category: ")
                if category == "":
                    print("Category is required.!")
                    continue
                else:
                    break

            description = input("Enter expense description (optional/press enter to skip): ")
            expenses.append({
                "amount": amount,
                "category": category,
                "description": description
            })
            print("expense added successfully.")
            break

def view_expenses(expenses):
    if len(expenses) == 0:
        print("There is no expenses to view it.")
    else:
        for i in range(len(expenses)):
            print(f"[{i}] - amount: {expenses[i]['amount']}$ , Category: {expenses[i]['category']}, "
            + f"Description: {expenses[i]['description']}")


def total_spent(expenses):
    if len(expenses) == 0:
        print("Total expenses = 0$")
    else:
        totalSpent = 0
        for expense in expenses:
            totalSpent += expense["amount"]
        print(f"Total expenses = {totalSpent:,}$")


def category_breakdown(expenses):
    if len(expenses) == 0:
        print("There is no expenses to view category breakdown for it.")
    else:
        categoryBreakdown = {}
        for expense in expenses:
            if expense["category"] not in categoryBreakdown:
                categoryBreakdown[expense["category"]] = expense["amount"]
            else:
                categoryBreakdown[expense["category"]] += expense["amount"]
        
        for category in categoryBreakdown:
            print(f"Category: {category} -> {categoryBreakdown[category]}$")

main()