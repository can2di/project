from flask import Flask, render_template, request, flash, url_for, redirect
from flask_login import login_user, login_required, logout_user
from models import User, Transaction, Category, db
from forms import TransactionForm, CategoryForm, ReportForm, LoginForm, RegisterForm
from flask_login import LoginManager, login_user, logout_user, current_user, login_required
import matplotlib.pyplot as plt
import io
import base64


class Controller:

    def __init__(self, app):
        self.app = app

        # Initialize Flask-Login
        login_manager = LoginManager(app)
        login_manager.login_view = 'login'
        @login_manager.user_loader
        

        @login_manager.user_loader
        def load_user(user_id):
            return User.query.get(int(user_id))

        @app.route('/login', methods=['GET', 'POST'])
        def login():
            form = LoginForm()
            if form.validate_on_submit():
                user = User.query.filter_by(username=form.username.data).first()               
                if user and user.check_password(form.password.data):
                    print(user.username)
                    # if user.is_active == True:
                    #     print(user.username)

                    login_user(user, remember=form.remember_me.data)
                    # if user.is_active == True:
                    #     print(user.username)
                    return redirect(url_for('index')) 
                else:
                    flash('Invalid username or password', 'danger')
                    return redirect(url_for('login'))
            return render_template('login.html', form=form)
        
        
        @app.route('/logout')
        def logout():
            logout_user()
            return redirect(url_for('login')) 
        

        @app.route('/register', methods=['GET', 'POST'])
        def register():
            form = RegisterForm()
            if form.validate_on_submit():
                user = User(username=form.username.data, email=form.email.data, password=form.password.data)
                db.session.add(user)
                db.session.commit()
                return redirect(url_for('index'))
            return render_template('register.html', form=form)

        @app.route('/', methods=['GET', 'POST'])
        @login_required
        def index():           
            return render_template('index.html')
       
        @app.route('/add', methods=['GET', 'POST'])
        @login_required
        def add():
            tform = TransactionForm()
            if tform.validate_on_submit():
                type = tform.type.data
                amount = tform.amount.data
                category = tform.category.data
                date = tform.date.data
                description = tform.description.data

                transaction = Transaction(type, amount, category, date, description)
                db.session.add(transaction)
                db.session.commit()

                flash('Transaction successfully added!')
                return render_template('add.html', form=tform)  
            return render_template('add.html', form=tform)
        
        @self.app.route('/view')
        @login_required
        def manage():
            transactions = Transaction.query.all() 
            return render_template('view_all_transactions.html', transactions=transactions)

        
        @app.route('/edit/<int:transaction_id>', methods=['GET', 'POST'])
        def edit_transaction(transaction_id):
            transaction = Transaction.query.get_or_404(transaction_id)
            form = TransactionForm(obj=transaction)  

            if form.validate_on_submit():
                transaction.type = form.type.data
                transaction.amount = form.amount.data
                transaction.category = form.category.data
                transaction.date = form.date.data
                transaction.description = form.description.data
                db.session.commit()
                flash('Transaction updated successfully!')
                return redirect(url_for('manage'))

            return render_template('edit_transaction.html', form=form)

        
        @app.route('/delete/<int:transaction_id>')
        def delete_transaction(transaction_id):
            transaction = Transaction.query.get_or_404(transaction_id)
            transaction.delete()
            flash('Transaction deleted successfully!')
            return redirect(url_for('manage'))
        
        @app.route('/manage', methods=['GET', 'POST'])
        @login_required
        def add_category():
            form = CategoryForm()
            category = Category.query.all() 
            if form.validate_on_submit():
                new_category = Category(name=form.name.data) 
                db.session.add(new_category)
                db.session.commit()
                category = Category.query.all() 
                render_template('manage.html', form=form, category=category) 
            return render_template('manage.html', form=form, category=category)
        

        @app.route('/dashboard')
        @login_required
        def dashboard():
            transactions = Transaction.query.all()
            income = 0
            expense = 0
            for transaction in transactions:
                if transaction.type.lower() == 'income':
                    income += float(transaction.amount)  # Assuming amount is a string representing a number
                else:
                    expense += float(transaction.amount)
            labels = ['Income', 'Expense']
            values = [income, expense]
            plt.bar(labels, values)
            plt.xlabel('Type')
            plt.ylabel('Amount in £s')
            plt.title('Income vs Expense')
            img = io.BytesIO()
            plt.savefig(img, format='png')
            img.seek(0)
            plt.close()
            img_base64 = base64.b64encode(img.getvalue()).decode('utf-8')

            return render_template('dashboard.html', income=income, expense=expense, chart_image=img_base64)
        
        @app.route('/reports', methods=['GET', 'POST'])
        @login_required
        def reports():
            form = ReportForm()

            if form.validate_on_submit():
                type_filter = form.type.data

        
                if type_filter == 'income':
                    transactions = Transaction.query.filter_by(type='Income').all()
                elif type_filter == 'expense':
                    transactions = Transaction.query.filter_by(type='Expense').all()
                else:
                    transactions = Transaction.query.all()

                return render_template('reports.html', transactions=transactions, form=form)

            return render_template('reports.html', form=form)

           
        
        