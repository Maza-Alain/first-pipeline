from flask import Flask

app = Flask(__name__)

@app.route('/sumar/<int:num1>/<int:num2>')
def sumar(num1, num2):
    resultado = num1 + num2
    return 'La suma de {} y {} es: {}'.format(num1, num2, resultado)

@app.route('/restar/<int:num1>/<int:num2>')
def restar(num1, num2):
    resultado = num1 - num2
    return 'La resta de {} menos {} es: {}'.format(num1, num2, resultado)

@app.route('/multiplicar/<int:num1>/<int:num2>')
def multiplicar(num1, num2):
    resultado = num1 * num2
    return 'El producto de {} y {} es: {}'.format(num1, num2, resultado)

if __name__ == '__main__':
    app.run(debug=True)
