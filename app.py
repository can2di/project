# from flask import Flask
# from controller.ExpenseController import ExpenseController
# from database.Database import Database

# app = Flask(__name__)
# expense_controller = ExpenseController(app)

# if __name__ == "__main__":
#     db = Database('expenses.db')
#     db.load_data('Income', '£2.00', 'Household', 'Toilet roll')
#     db.load_data('Expense', '£300.00', 'Leisure', 'Gym')
#     db.load_data('Income', '£40.0', 'Food', 'KFC')
#     db.load_data('Expense', '£2.75', 'Drink', 'Winemark')
    

#     print('Database has been created')
#     app.run(debug=True)
   

# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy import create_engine
# from sqlalchemy import inspect

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
# db = SQLAlchemy(app)

# class User(db.Model):
#     __tablename__ = 'users'
#     id = db.Column(db.Integer, primary_key=True)
#     username = db.Column(db.String(80), unique=True, nullable=False)

#     email = db.Column(db.String(120), unique=True, nullable=False)
#     password = db.Column(db.String(80), nullable=False)

# with app.app_context():
#     engine = create_engine('sqlite:///mydatabase.db')  # Create the engine here
#     inspector = inspect(engine)
#     db.create_all()

#     for table_name in inspector.get_table_names():
#         print('Tables')
#         print(table_name)

# if __name__ == '__main__':
#     app.run(debug=True)

# Step 1: Import the necessary modules

# from sqlalchemy import create_engine, Column, Integer, String, DateTime
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker
# import datetime



# # Step 2: Establish a database connection

# database_url = 'sqlite:///your_database_name.db'

# # Create an engine to connect to a SQLite database
# engine = create_engine(database_url)

# #will return engine instance
# Base = declarative_base()

# # Step 3: Define your data model
# class User(Base):
#     __tablename__ = 'users'

#     id = Column(Integer, primary_key=True)
#     username = Column(String(50), unique=True, nullable=False)
#     email = Column(String(100), unique=True, nullable=False)
#     password = Column(String(100), unique=True, nullable=False)
#     created_at = Column(DateTime, default=datetime.datetime.utcnow)

# # Step 4: Create the database tables
# Base.metadata.create_all(engine)

# # Step 5: Insert data into the database
# Session = sessionmaker(bind=engine)
# session = Session()

# # Example: Inserting a new user into the database
# new_user = User(username='Sandy', email='dan@gmail.com', password='password')
# session.add(new_user)
# session.commit()

# # Step 6: Query data from the database
# # Example: Querying all users from the database
# all_users = session.query(User).all()

# # Example: Querying a specific user by their username
# user = session.query(User).filter_by(username='Sandy').first()

# # Step 7: Close the session
# session.close()


# from flask import Flask, render_template, request, flash, url_for, redirect
# from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
# app.config['SECRET_KEY'] = "random string"

# db = SQLAlchemy(app)

# class Student(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100), nullable=False)
#     city = db.Column(db.String(50), nullable=False)
#     addr = db.Column(db.String(200), nullable=False)
#     pin = db.Column(db.String(10), nullable=False)

#     def __repr__(self):
#         return f"<Student {self.name}>"

# @app.route('/')
# def show_all():
#     students = Student.query.all()
#     return render_template('show_all.html', students=students)

# @app.route('/new', methods=['GET', 'POST'])
# def new():
#     if request.method == 'POST':
#         if not request.form['name'] or not request.form['city'] or not request.form['addr'] or not request.form['pin']:
#             flash('Please enter all the fields', 'error')
#         else:
#             student = Student(name=request.form['name'],
#                               city=request.form['city'],
#                               addr=request.form['addr'],
#                               pin=request.form['pin'])
#             db.session.add(student)
#             db.session.commit()
#             flash('Record was successfully added')
#             return redirect(url_for('show_all'))

#     return render_template('new.html')

# with app.app_context():
#     db.create_all()


# if __name__ == '__main__':
#     app.run(debug=True)



from flask import Flask, render_template, request, flash, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from wtforms import StringField, PasswordField, SubmitField,validators
from wtforms.validators import DataRequired, Email
from flask_wtf import FlaskForm
# from Student import Student, db
from studentform import StudentForm
from views import Controller
from models import db



app = Flask(__name__)
controller = Controller(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
app.config['SECRET_KEY'] = "random string"


db.init_app(app)







with app.app_context():
    db.create_all()


if __name__ == '__main__':
    app.run(debug=True)

# from flask import Flask, render_template, request, flash, url_for, redirect
# from flask_sqlalchemy import SQLAlchemy
# from wtforms import StringField, PasswordField, SubmitField,validators
# from wtforms.validators import DataRequired, Email
# from flask_wtf import FlaskForm
# from model.student import Student

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
# app.config['SECRET_KEY'] = "random string"

# db = SQLAlchemy(app)


# class StudentForm(FlaskForm):
#     name = StringField('Name', validators=[validators.DataRequired()])
#     city = StringField('City', validators=[validators.DataRequired()])
#     addr = StringField('Address', validators=[validators.DataRequired()])
#     pin = StringField('PIN', validators=[validators.DataRequired(), validators.Length(min=4, max=10)])  # Add length validation

#     submit = SubmitField('Submit')

# @app.route('/')
# def show_all():
#     students = Student.query.all()
#     return render_template('show_all.html', students=students)

# @app.route('/new', methods=['GET', 'POST'])
# def new():
#     form = StudentForm()  # Create a form instance
#     if form.validate_on_submit():  # Check if form data is valid
#         student = Student(name=form.name.data,
#                           city=form.city.data,
#                           addr=form.addr.data,
#                           pin=form.pin.data)
#         db.session.add(student)
#         db.session.commit()
#         flash('Record was successfully added')
#         return redirect(url_for('show_all'))

#     return render_template('new.html', form=form)

# with app.app_context():
#     db.create_all()


# if __name__ == '__main__':
#     app.run(debug=True)


# from flask import Flask, render_template, request, flash, url_for, redirect
# from flask_sqlalchemy import SQLAlchemy
# from flask_wtf import FlaskForm
# from forms.studentform import studentform # Import StudentForm
# from model.student import student  # Import Student class

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
# app.config['SECRET_KEY'] = "random string"

# db = SQLAlchemy(app)

# @app.route('/')
# def show_all():
#     students = student.query.all()
#     return render_template('show_all.html', students=students)


# @app.route('/new', methods=['GET', 'POST'])
# def new():

#     form = studentform()  # Create a form instance
#     if form.validate_on_submit():  # Check if form data is valid
#         student = student(name=form.name.data,
#                           city=form.city.data,
#                           addr=form.addr.data,
#                           pin=form.pin.data)
#         db.session.add(student)
#         db.session.commit()
#         flash('Record was successfully added')
#         return redirect(url_for('show_all'))

#     return render_template('new.html',form=form)


# with app.app_context():
#     db.create_all()


# if __name__ == '__main__':
#     app.run(debug=True)


# from flask import Flask, render_template, request, flash, url_for, redirect
# from flask_sqlalchemy import SQLAlchemy
# from wtforms import StringField, PasswordField, SubmitField, validators
# from wtforms.validators import DataRequired, Email
# from flask_wtf import FlaskForm
# from Student import Student  # Import Student class

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.db'
# app.config['SECRET_KEY'] = "random string"

# db = SQLAlchemy(app)

# class StudentForm(FlaskForm):
#     name = StringField('Name', validators=[validators.DataRequired()])
#     city = StringField('City', validators=[validators.DataRequired()])
#     addr = StringField('Address', validators=[validators.DataRequired()])
#     pin = StringField('PIN', validators=[validators.DataRequired(), validators.Length(min=4, max=10)])  # Add length validation

#     submit = SubmitField('Submit')

# @app.route('/')
# def show_all():
#     students = Student.query.all()
#     return render_template('show_all.html', students=students)

# @app.route('/new', methods=['GET', 'POST'])
# def new():
#     form = StudentForm()  # Create a form instance
#     if form.validate_on_submit():  # Check if form data is valid
#         student = Student(name=form.name.data,
#                           city=form.city.data,
#                           addr=form.addr.data,
#                           pin=form.pin.data)
#         db.session.add(student)
#         db.session.commit()
#         flash('Record was successfully added')
#         return redirect(url_for('show_all'))

#     return render_template('new.html', form=form)

# with app.app_context():
#     db.create_all()


# if __name__ == '__main__':
#     app.run(debug=True)


