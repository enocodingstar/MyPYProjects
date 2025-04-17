import csv
import os

class Expense:
    def __init__(self, amount, date):
        self.amount = amount
        self.date = date
        self.category = None

    def __str__(self):
        return f"Amount: ${self.amount}, Date: {self.date}, Category: {self.category}"
    

class ExpenseCategorizer:
    def __init__(self, filename= "Expenses.csv"):
        self.expenses = []
        self.filename = filename

        if not os.path.exists(self.filename):
            with open(self.filename, "w", newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Amount ($)", "Category", "Date"])

    def addExpenses(self, expense):
        if expense.amount > 0 and (expense.amount < 100 or expense.amount == 100):
            expense.category = "minor"
        elif expense.amount > 100 and (expense.amount < 1000 or expense.amount == 1000):
            expense.category = "moderate"
        elif expense.amount > 1000 and (expense.amount < 10000 or expense.amount == 10000):
            expense.category = "major"
        else:
            print("Expense amount beyond range.")
            return
        self.expenses.append(expense)
        print("Expense has been added.")

        with open(self.filename, "a", newline='') as file:
            writer = csv.writer(file)
            writer.writerow([expense.amount, expense.category, expense.date])


    def viewExpenses(self):
        if not self.expenses:
            print("No expenses to show.")
            return
        for expense in self.expenses:
            print(expense)


def main():
    myExpenses = ExpenseCategorizer()
    while True:
        print("Welcome to the Expense Tracker App.\n You add expenses while we categorize them. \n Hope you enjoy using the app.")
        print("Choose from the following options: \n"
              "1. Add an expense\n"
              "2. View all expenses\n" \
              "3. Exit the app")
        
        try:
            choice = int(input("Choose an option (1-3): "))
        except ValueError:
            print("Invalid input. Enter a valid choice.")
        else:
            if choice == 1:
                amount = int(input("Enter the expense amount: "))
                date = input("Enter the date: ")
                myExpenses.addExpenses(Expense(amount, date))
            elif choice == 2:
                myExpenses.viewExpenses()
            elif choice == 3:
                print("Thanks for using the app. Hope to see you another time. \n"
                      "Exiting the app....")
            else:
                print("Invalid choice. Choose an option between (1-3).")





if __name__ == "__main__":
    main()