from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    
    return render_template('index.html')  

@app.route('/login')
def login():
   
    return render_template('login.html')  

@app.route('/dashboard')
def dashboard():
    
    return render_template('dashboard.html')  

@app.route('/add')
def add():
    
    return render_template('add.html')  

@app.route('/view')
def view():
    
    return render_template('view.html')  

@app.route('/manage')
def manage():
    
    return render_template('manage.html')

@app.route('/reports')
def reports():
    
    return render_template('reports.html') 





if __name__ == '__main__':
    app.run(debug=True)  # Run the app in debug mode for automatic reloading
 