from flask import render_template, Flask, request, jsonify
from database.Database import Database

class ExpenseController:

    def __init__(self, app):
        self.app = app
        @self.app.route('/')
        def index():
            # db = Database('expenses.db')
            # db.read_data()
            return render_template('index.html')

        @self.app.route('/sort' , methods=['POST'])
        def sort():
            db = Database('expenses.db')
            data = db.sort_data
            db.close_connection()
            print('sort')
            return render_template('view.html', data=data)
        
        @self.app.route('/view')
        def view():
            db = Database('expenses.db')
            data = db.fetch_all_data()
            db.close_connection()
            return render_template('view.html', data=data)

        @self.app.route('/add')
        def add():    
           return render_template('add.html')


        @self.app.route('/add_expense', methods=['GET', 'POST'])
        def add_expense():
            if request.method == 'POST':
                type = request.form['type']
                amount = request.form['amount']
                category = request.form['category']
                description = request.form['description']
                print(amount)
                db = Database('expenses.db')
                db.load_data(type, amount, category, description)
                return render_template('success.html')
 
        @app.route('/edit/<int:id>')
        def edit_expense(id):
            db = Database('expenses.db')
            expense = db.get_expense_by_id(id)
            print(f"Expense ID: {expense}")
            return render_template('edit_expense.html', expense=expense)

        @self.app.route('/delete/<int:id>')
        def delete(id):
            
            db = Database('expenses.db')
            print("Delete row")
            db.delete_expense(id)
            data = db.fetch_all_data()
            return render_template('view.html', data=data)




