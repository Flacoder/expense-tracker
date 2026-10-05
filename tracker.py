# Header Comment: Installment 2
# Author: Charles Gian T. Quiocho

print("=" * 40)
print("EXPENSE TRACKER".center(40))
print("Know where your money goes.".center(40))
print("=" * 40)


print("\nMAIN MENU")
print("    [1] Add an expense         (coming soon)")
print("    [2] View all expenses      (coming soon)")
print("    [3] Show total spent       (coming soon)")
print("    [4] Exit                   (coming soon)\n")


name = input("What's your name? ")
print(f"Welcome, {name}! Let's log two expenses.\n")


item1 = input("First expense? ")
amount1 = float(input("Amount? "))
item2 = input("Second expense? ")
amount2 = float(input("Amount? "))


total = amount1 + amount2
average = total / 2


print("\n" + "-" * 40)
print("SUMMARY")
print(f"    - {item1 + ':':<10} ${amount1}")
print(f"    - {item2 + ':':<10} ${amount2}")
print(f"{'Total spent:':<15} ${total}")
print(f"{'Average:':<15} ${average}")
print("-" * 40)


print("Made by: Charles Gian T. Quicoho  |  Installment 2")