from datetime import datetime
from flask import render_template
from MySiteTest import app
from MySiteTest.visualization import build_plot

@app.route('/')
def home():
    return render_template(
        'home.html',
        title='Home',
        time=datetime.now(),
    )


@app.route('/_add_numbers')
def add_numbers():
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    return jsonify(result=a + b)

@app.route('/datasets')
def datasets():

    return render_template(
        'datasets.html',
        title='Datasets',
        time=datetime.now(),
        message='clean your data',
    )

@app.route('/training')
def training():

    return render_template(
        'training.html',
        title='Training',
        time=datetime.now(),
        message='train your model',
    )

@app.route('/visualization')
def visualization():
    plot_snippet = build_plot()
    return render_template(
        'visualization.html',
        title='Visualization',
        time=datetime.now(),
        message='take your result', 
    )

@app.route('/test')
def test():
    """Renders the about page."""
    return render_template(
        'test.html',
        title='Test',
        time=datetime.now(),
        message='test your model',
    )

@app.route('/browser')
def browser():
    """Renders the about page."""
    return render_template(
        'browser.html',
        title='Browser',
        time=datetime.now(),
        message='search for knowladge',

    )

@app.route('/signin')
def signin():
    """Renders the about page."""
    return render_template(
        'signin.html',
        title='Signin',
        time=datetime.now(),
        message='only for administrator'
    )

@app.route('/signup')
def signup():
    """Renders the about page."""
    return render_template(
        'signup.html',
        title='Signup',
        time=datetime.now(),
        message='not aviliable'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        time=datetime.now(),
        message='about me'
    )