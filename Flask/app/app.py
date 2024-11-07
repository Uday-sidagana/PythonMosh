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

#HTML and Template Handling along with URL redirection and dynamic urls

'''from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__, template_folder='templates')

@app.route('/')
def hello():
    firstname = "Sidagana"
    lastname= "Kiran"
    myage=10 + 11
    mylist =[10,20,30,40,50]
    
    return render_template('index.html', a=firstname, b=lastname, c =myage, d=mylist)

@app.route('/filter')
def filter():
    text = "Uday Sidagana"
    return render_template("filter.html", text = text)

@app.route('/redirect_endpoint')
def redirect_endpoint():
    return redirect(url_for('filter'))  #Using url_for() without redirect function returns a value "/filter"

#Custom filter
@app.template_filter('reverse_string')
def string_reverse(s):
    return s[::-1] #(first : is for parsing through entire string, second : is to step back(-1), effectively reversing string)

@app.template_filter("repeat")
def repeat(s,times=2):
    return s*times

@app.template_filter('alternate_case')
def alt_case(s):
    new =""
    for i in s:
        
        if i.isupper():
            i= i.lower()
            
        elif i.islower():
            i= i.upper()
        new = new + i
    return new

@app.template_filter('ind_alt_case')
def ind_alt_case(s):
    return ''.join(c.upper() if i%2 ==0 else c.lower() for i,c in enumerate(s))
    

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port= 5500, debug =True)'''


#Forms, POST, JSON handling, File Handling
from flask import Flask, render_template, request, redirect

app = Flask(__name__, template_folder='templates2')

@app.route('/', methods =['GET', 'POST'])
def index():
    if request.method == 'GET':
        a = "Uday"
        return render_template('index.html', name=a)
    elif request.method == 'POST':
        if 'username' in request.form.keys() and 'password' in request.form.keys() and request.form.get('username') and request.form.get('password'):
            username = request.form.get('username')
            password = request.form['password']
            if username == 'Panda' and password == 'pubg':
                return f"Your username is {username} and password is {password} \n Success!!"
            else:
                return "Bruh You ain't the panda I know!!"
        else:
            return "Please fill up the Fields!"
        

@app.route('/file_upload')
def file_upload():
    pass

if __name__ == "__main__":
    app.run(host = '0.0.0.0', port=5200, debug=True)