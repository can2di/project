from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    """Renders the home page"""
    return render_template('index.html')  # Assuming you have a home.html template

@app.route('/about/<name>')
def about(name):
    """Renders the about page"""
    return render_template('about.html', name=name)  # Assuming you have an about.html template

@app.route('/contact')
def contact():
    """Renders the contact page"""
    return render_template('contact.html')  # Assuming you have a contact.html template

@app.route('/products/<product_id>')
def product(product_id):
    """Renders the product page with a dynamic product ID"""
    # You can retrieve product details here based on product_id
    product_name = f"Product {product_id}"
    return render_template('product.html', product_name=product_name)

@app.route('/blog')
def blog():
    """Renders the blog page (can be further enhanced with blog posts)"""
    return render_template('blog.html')  # Assuming you have a blog.html template

if __name__ == '__main__':
    app.run(debug=True)  # Run the app in debug mode for automatic reloading
 