# Put your app in here.
from flask import Flask, request
from operations import add, sub, mult, div
app = Flask(__name__)

@app.route('/add')
def return_sum():
    a = int(request.args["a"])
    b = int(request.args["b"])
    return f"<body>{add(a,b)}</body>"

@app.route('/sub')
def return_dif():
    a = int(request.args["a"])
    b = int(request.args["b"])
    return f"<body>{sub(a,b)}</body>"

@app.route('/mult')
def return_product():
    a = int(request.args["a"])
    b = int(request.args["b"])
    return f"<body>{mult(a,b)}</body>"

@app.route('/div')
def return_quotient():
    a = int(request.args["a"])
    b = int(request.args["b"])
    return f"<body>{div(a,b)}</body>"

math_operations = {"add": add,
                   "sub": sub,
                   "mult": mult,
                   "div": div}

@app.route('/math/<operation>')
def calculate(operation):
    a = int(request.args["a"])
    b = int(request.args["b"])

    #result = math_operations[operation](a,b) 
    function = math_operations.get(operation)

    if(not function):
        return f"<body>Invalid operation. Valid operations are: add, sub, mult, and div.</body>"
    else: 
        result = function(a,b)
        return f"<body>{result}</body>"
