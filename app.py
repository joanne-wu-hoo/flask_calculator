from flask import Flask, request
from operations import add, sub, mult, div
app = Flask(__name__)

# Part 1: Create 4 separate routes to add, subtract, multiply, and divide two numbers
@app.route('/add')
def return_sum():
    """Add a and b parameters. Return result."""
    a = int(request.args["a"])
    b = int(request.args["b"])
    return f"<body>{add(a,b)}</body>"

@app.route('/sub')
def return_dif():
    """Subtract a and b parameters. Return result."""
    a = int(request.args["a"])
    b = int(request.args["b"])
    return f"<body>{sub(a,b)}</body>"

@app.route('/mult')
def return_product():
    """Multiply a and b parameters. Return result."""
    a = int(request.args["a"])
    b = int(request.args["b"])
    return f"<body>{mult(a,b)}</body>"

@app.route('/div')
def return_quotient():
    """Divide a and b parameters. Return result."""
    a = int(request.args["a"])
    b = int(request.args["b"])
    return f"<body>{div(a,b)}</body>"

# Part 2: Create one route to execute requested operation?

# Dictionary to map requested operation with the corresponding function from operations.py
math_operations = {"add": add,
                   "sub": sub,
                   "mult": mult,
                   "div": div}

@app.route('/math/<operation>')
def calculate(operation):
    """Execute requested operation on a and b parameters. Return result."""
    a = int(request.args["a"])
    b = int(request.args["b"])

    function = math_operations.get(operation)

    if(not function):
        return f"<body>Invalid operation. Valid operations are: add, sub, mult, and div.</body>"
    else: 
        result = function(a,b)
        return f"<body>{result}</body>"
