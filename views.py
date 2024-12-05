from flask import Flask, render_template, request, flash, url_for, redirect
from flask_login import login_user, login_required, logout_user
from models import User, Transaction, db
from forms import UserForm, TransactionForm, LoginForm, RegisterForm
class Controller:

    def __init__(self, app):
        self.app = app

        @app.route('/', methods=['GET', 'POST'])
        def logins():
            form = UserForm()
            print('right')
            if form.validate_on_submit():
                user = User.query.filter_by(user=form.user.data).first()
                print('right')
                if user and user.check_password(form.password.data):
                    login_user(user)
                    flash('Login successful!')
                    print('right')
                    return redirect(url_for('manage'))
  
                else:
                    flash('Invalid username or password')
                    print('Wrong')
                    return render_template('register.html')
            print('dasd')
            return render_template('login.html')



        # @app.route('/register', methods=['GET', 'POST'])
        # def register():
        #     form = RegisterForm() 
        #     if form.validate_on_submit():  # Check if form data is valid
        #         userAA = User(user=form.user.data,
        #                   password=form.password.data)
        #         userAA.set_password(password=form.password.data)
        #         db.session.add(userAA)
        #         db.session.commit()
        #         flash('Record was successfully added')

        #         return render_template('register.html', form=form)
        #     return render_template('register.html', form=form)
        
        
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
                return render_template('add.html', form=tform)  # Render after successful submission
            return render_template('add.html', form=tform)  # Render the form on GET request
        
        @self.app.route('/manage')
        def manage():
            transactions = Transaction.query.all()  # Fetch all transactions
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
        
        @app.route('/login', methods=['GET', 'POST'])
        def login():
            form = LoginForm()
            if form.validate_on_submit():
                user = User.query.filter_by(username=form.username.data).first()
                
                if user and user.check_password(form.password.data):
                    login_user(user, remember=form.remember_me.data)
                    return redirect(url_for('manage'))  # Replace 'index' with your desired redirect
                else:
                    flash('Invalid username or password', 'danger')
                    return redirect(url_for('manage'))
            return render_template('login.html', form=form)
        

        @app.route('/register', methods=['GET', 'POST'])
        def register():
            form = RegisterForm()
            if form.validate_on_submit():
        # Create a new user instance
                user = User(username=form.username.data, email=form.email.data, password=form.password.data)
        # Add the new user to the database
                db.session.add(user)
                db.session.commit()
        # Redirect to a success page or login page
                return redirect(url_for('login'))
            return render_template('register.html', form=form)
        