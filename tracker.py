# Project: Expense Tracker - Installment 4
# Author: Charles Gian T. Quiocho
# Description: This evaluates expense sizes, checks for warnings, and determines the budget verdict.

print("========================================")
print("            EXPENSE TRACKER             ")
print("      Know where your money goes.       ")
print("========================================")

name = input("What's your name? ")
tax_percent = float(input("Tax rate %? "))
budget = float(input("Your budget? "))
print(f"Welcome, {name}!")

subtotal = 0.0
count = 0

menu_text = """MAIN MENU
  [1] Add an expense        
  [2] View all expenses     (coming soon)
  [3] Show total spent      
  [4] Exit                  """

while True:
    print()
    print(menu_text)
    choice = input("Choose 1-4: ")

    if choice == "1":
        amount = float(input("Amount? "))
        subtotal += amount
        count += 1
        if amount > 200:
            print("  Huge expense - are you sure?")
        elif amount > 100:
            print("  Big expense.")
        elif amount > 50:
            print("  Moderate expense.")
        else:
            print("  Small expense.")
            
    elif choice == "2":
        print("Coming soon: the tracker can't remember each item yet.")
        
    elif choice == "3":
        tax_amount = subtotal * (tax_percent / 100)
        grand_total = subtotal + tax_amount
        over_budget = grand_total - budget
        left_in_budget = budget - grand_total

        print(f"Expenses:    {count}")
        print(f"Subtotal:    ${subtotal}")
        print(f"Tax ({tax_percent}%):".ljust(13) + f"${tax_amount}")
        print(f"Grand total: ${grand_total}")

        if grand_total > budget:
            print(f"Over budget by ${over_budget}!")
        elif grand_total > 0.90 * budget:
            print(f"Careful: only ${left_in_budget} left.")
        else:
            print(f"Within budget. ${left_in_budget} left.")
        
    elif choice == "4":
        print(f"Goodbye, {name}!")
        print("-" * 40)
        print(f"Made by: Charles Quiocho  |  Installment 5")
        print("========================================")
        break
        
    else:
        print("Please choose 1, 2, 3 or 4.")