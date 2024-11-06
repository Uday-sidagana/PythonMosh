'''from flask import Flask, request, make_response


app = Flask(__name__)

@app.route('/')
def index():
    response = make_response("Hello")
    response.status_code = 500
    response.headers["Content-Type"] = 'applications/octet-stream'
    #response.headers["Content-Length"] = 20
    #return "<h1>Hello</h1>", 500
    return response

@app.route('/greet/<name>')
def greet(name):
    return f"Hello {name}"

@app.route('/add/<int:n1>/<int:n2>')
def add (n1, n2):
    return f"{n1+n2}"

@app.route('/handle_url_params')
def handle_params():
    if "greetings" in request.args.keys() and "name" in request.args.keys():
        # return str(request.args)
        greetings = request.args['greetings']#Dict key value pair
        names = request.args.get('name')#get keyword
        return f"{greetings}, {names}"
    else:
        return "Error 404(Params missing)"
    
@app.route('/Get_Post_Put_Delete', methods=['GET','POST','PUT','DELETE'])
def method_test():
    if request.method == 'GET':
        return "GET"
    elif request.method == "POST":
        return "POST"
    else:
        "You'll never see this message"


if __name__ == "__main__":
    app.run(host= '127.0.0.1', port=5000, debug=True)'''


from flask import Flask, request, render_template

app = Flask(__name__, template_folder='templates')

@app.route('/')
def hello():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port= 5000, debug =True)