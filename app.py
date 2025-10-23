from flask import Flask

app = Flask(__name__)


@app.route("/hello")
def say_hello(name):		# Function
    return f"Hello, {name}!"

@app.route('/<int:num1>/<string:operation>/<int:num2>')		# Route	
def calc(num1, operation, num2):
    if operation == "add":
        result = num1 + num2
        return f'{num1} + {num2} = {result}'
if __name__ == '__main__':

    app.run(debug=True)

