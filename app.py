from flask import Flask
from controller.ExpenseController import ExpenseController
from database.Database import Database

app = Flask(__name__)
expense_controller = ExpenseController(app)

if __name__ == "__main__":
    db = Database('expenses.db')
    db.load_data('Income', '£2.00', 'Household', 'Toilet roll')
    db.load_data('Expense', '£300.00', 'Leisure', 'Gym')
    db.load_data('Income', '£40.0', 'Food', 'KFC')
    db.load_data('Expense', '£2.75', 'Drink', 'Winemark')
    

    print('Database has been created')
    app.run(debug=True)
   