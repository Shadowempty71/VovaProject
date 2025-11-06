from flask import Flask
from flask import request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Привет, мир!"

@app.route("/calc/<operator>")
def calc(operator):
    nums = request.args.get("nums")
    nums_array = nums.split(',')
    x, y = nums_array[0], nums_array[1]
    x,y = int(x),int(y)

    if operator == "plus":
        res = x + y
        return str(res)
    elif operator == "minus":
        res = x - y
        return x - y
    else:
        return "Error!"