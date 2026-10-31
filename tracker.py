# Project: Expense Tracker - Installment 3
# Author: Charles Gian T. Quiocho
# Description: This calculates the subtotal, tax rate, grand total, budget status, and remaining budget.

print("========================================")
print("            EXPENSE TRACKER             ")
print("      Know where your money goes.       ")
print("========================================")
print("MAIN MENU")
print("  [1] Add an expense        (coming soon)")
print("  [2] View all expenses     (coming soon)")
print("  [3] Show total spent      (coming soon)")
print("  [4] Exit                  (coming soon)")
print()

name = input("What's your name? ")
print(f"Welcome, {name}! Let's log two expenses.")

expense1_name = input("First expense? ")
amount1 = float(input("Amount? "))
if amount1 > 200:
    print("  Huge expense - are you sure?")
elif amount1 > 100:
    print("  Big expense.")
elif amount1 > 50:
    print("  Moderate expense.")
else:
    print("  Small expense.")

expense2_name = input("Second expense? ")
amount2 = float(input("Amount? "))
if amount2 > 200:
    print("  Huge expense - are you sure?")
elif amount2 > 100:
    print("  Big expense.")
elif amount2 > 50:
    print("  Moderate expense.")
else:
    print("  Small expense.")

tax_rate = float(input("Tax rate %? "))
budget = float(input("Your budget? "))

if amount1 > 100 and amount2 > 100:
    print("  Two big expenses in a row - slow down!")

subtotal = amount1 + amount2
average = subtotal / 2
tax_amount = subtotal * (tax_rate / 100)
grand_total = subtotal + tax_amount

over_budget = grand_total - budget
left_in_budget = budget - grand_total

print("-" * 40)
print("SUMMARY")
print(f"  - {expense1_name:<9} ${amount1:.2f}")
print(f"  - {expense2_name:<9} ${amount2:.2f}")
print(f"Subtotal:    ${subtotal:.2f}")
print(f"Average:     ${average:.2f}")
print(f"Tax ({tax_rate}%):".ljust(13) + f"${tax_amount:.2f}")
print(f"Grand total: ${grand_total:.2f}")

if grand_total > budget:
    print(f"Over budget by ${over_budget:.2f}!")
elif grand_total > 0.90 * budget:
    print(f"Careful: only ${left_in_budget:.2f} left.")
else:
    print(f"Within budget. ${left_in_budget:.2f} left.")

print("-" * 40)
print("Made by: Charles Gian Quiocho  |  Installment 4")