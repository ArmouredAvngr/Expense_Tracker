import os
import csv

home = os.path.expanduser("~")
file_path = os.path.join(home, "Documents", "Expenses.csv")


with open(file_path, mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Category", "Expense", "Remaining Budget"])

budget = float(input("Enter your budget: "))

while True:
    expense = float(input("Enter your expense (how much you spent): "))
    category = input("Enter what you spent it on (e.g. gaming, health, groceries etc: ")

    budget = budget - expense

    if budget < 0:
        print("Warning! You are over budget!")

    with open(file_path, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([category, expense, budget])

    again = input("\nWould you like to log another expense? (y/n): ")

    if again != "y":
        print("\nAll expenses saved to:", file_path)
        break
        
    input("Press Enter to continue...")

