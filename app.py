from flask import Flask, render_template, redirect
from apiLoja import loja, user, venda, produtos

app = Flask(__name__)
app.register_blueprint(loja.loja)
app.register_blueprint(user.user)
app.register_blueprint(venda.venda)
app.register_blueprint(produtos.produtos)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET'])
def login():
    return render_template('entrar.html')

@app.route('/entrar', methods=['GET'])
def entrar():
    return redirect('login')

@app.errorhandler(404)
def rotaNaoEncontrada(Erro):
    return "Rota não Encontrada" + str(Erro)

@app.errorhandler(403)
def erroDePermissao(Erro):
    return "Não tem permissão" + str(Erro)