from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/') # Rota para o Index
def index():
    return render_template('index.html')

@app.route('/cadastro', methods=['GET', 'POST']) # Rota para o Cadastro
def cadastro():
    if request.method == 'POST':
        # Aqui pegaremos os dados do formulário depois
        pass
    return render_template('cadastro.html')

if __name__ == '__main__':
    app.run(debug=True)