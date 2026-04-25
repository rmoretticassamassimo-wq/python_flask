# Importa o Flask e a função de renderizar templates
from flask import Flask, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'TROCAR_SENHA'

# Rota principal chamando o arquivo HTML
from flask import Flask, render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'TROCAR_SENHA'

@app.route('/')
def index():
    titulo = "Painel de Controle"
    usuario_logado = "Raphael" 
    return render_template('index.html', titulo_pagina=titulo, nome_usuario=usuario_logado)

# É ESTA PARTE AQUI QUE LIGA O SERVIDOR!
# Tem que ter os dois "anderlines" (__) de cada lado da palavra
if __name__ == '__main__':
    app.run(debug=True)