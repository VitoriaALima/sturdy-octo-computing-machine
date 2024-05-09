from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', resultado='')


@app.route('/verificar', methods=['POST'])  # Define uma rota '/verificar' que aceita apenas requisições POST
def verificar():
    # Obtém o número enviado no formulário HTML e verifica a temperatura
    temp = 0
    temp = int(request.form['temp'])
    if (temp <= 37.2):
        resultado = "Temp normal"
    elif ((temp > 37.2) and (temp <= 38)):
        resultado = "Estado febril"
    elif ((temp > 38) and (temp <= 39)):
        resultado = "Com febre"
    else:
        resultado = "Febre alta"

    # Retorna o resultado da verificação diretamente no template 'index.html'
    return render_template('index.html', resultado = resultado)


if __name__ == '__main__':
    # Inicia o servidor Flask em modo de depuração se este script for executado diretamente
    app.run(debug=True)

