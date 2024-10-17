from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    current_time = datetime.now().strftime("%B %d, %Y %I:%M %p")
    return render_template('index.html', current_time=current_time)

@app.route('/user/<username>')
def user(username):
    return render_template('user.html', username=username)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)
