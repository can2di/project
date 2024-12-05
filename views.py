from flask import Flask, render_template, request, flash, url_for, redirect
from flask_login import login_user, login_required, logout_user
from models import User, Transaction, db
from forms import UserForm, TransactionForm, LoginForm, RegisterForm
from flask_login import LoginManager, login_user, logout_user, current_user, login_required


class Controller:

    def __init__(self, app):
        self.app = app

        # Initialize Flask-Login
        login_manager = LoginManager(app)
        login_manager.login_view = 'index' 

        @login_manager.user_loader
        def load_user(user_id):
            return User.query.get(int(user_id)) 

        @app.route('/login', methods=['GET', 'POST'])
        def login():
            form = LoginForm()
            if form.validate_on_submit():
                user = User.query.filter_by(username=form.username.data).first()
                if user and user.check_password(form.password.data):
                    login_user(user, remember=form.remember_me.data)
                    return redirect(url_for('index')) 
                else:
                    flash('Invalid username or password', 'danger')
                    return redirect(url_for('manage'))
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
                return redirect(url_for('login'))
            return render_template('register.html', form=form)

        @app.route('/', methods=['GET', 'POST'])
        def index():
            
            return render_template('index.html')


        
        @app.route('/add', methods=['GET', 'POST'])
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
        def manage():
            transactions = Transaction.query.all() 
            return render_template('view_all_transactions.html', transactions=transactions)

        
        @app.route('/edit/<int:transaction_id>', methods=['GET', 'POST'])
        def edit_transaction(transaction_id):
            transaction = Transaction.query.get_or_404(transaction_id)
            form = TransactionForm(obj=transaction)  # Pre-fill the form with transaction data

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
        
        
        