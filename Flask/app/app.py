from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Hello</h1>"

@app.route('/greet/<name>')
def greet(name):
    return f"Hello {name}"

@app.route('/add/<int:n1>/<int:n2>')
def add (n1, n2):
    return f"{n1+n2}"

@app.route('/adds')
def adds (n1, n2):
    return f"{n1+n2}"

if __name__ == "__main__":
    app.run(host= '127.0.0.1', port=5000, debug=True)