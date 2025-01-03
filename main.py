def add_expense(expenses,amount,category):
    expenses.append({'amount':amount,'category':category})

def print_expenses(expenses):
    for expense in expenses:
        print(f'Amount: {expense["amount"]}, Category: {expense["category"]}')

def total_Expenses(expenses):
    return sum(map(lambda expense : expense['amount'],expenses))

def filter_expenses(expenses,category):
    return filter(lambda expense: expense['category'] == category,expenses)

"""
    Expense Tracker
    This script allows the user to track their expenses by adding, listing, 
    calculating the total, and filtering expenses by category.
    Functions:
        Adds an expense to the expenses list.
        Prints all expenses in the expenses list.
        total_Expenses(expenses)
        Returns the total amount of all expenses.
        filter_expenses(expenses, category)
        Filters and returns expenses by the specified category.
        The main function that runs the expense tracker program.
"""

def main():
    expenses = []
    while True:
        print('\nExpense Tracker')
        print('1. Add an expense')
        print('2. List all expenses')
        print('3. Show total expenses')
        print('4. Filter expenses by category')
        print('5. Exit')
       
        choice = input('Enter your choice: ')

        if choice == '1':
            amount = float(input('Enter amount: '))
            category = input('Enter category: ')
            add_expense(expenses, amount, category)

        elif choice == '2':
            print('\nAll Expenses:')
            print_expenses(expenses)
    
        elif choice == '3':
            print('\nTotal Expenses: ', total_Expenses(expenses))
    
        elif choice == '4':
            category = input('Enter category to filter: ')
            print(f'\nExpenses for {category}:')
            expenses_from_category = filter_expenses(expenses, category)
            print_expenses(expenses_from_category)
    
        elif choice == '5':
            print('Exiting the program.')
            break

main()