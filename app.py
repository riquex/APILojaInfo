from flask import Flask
from apiLoja import loja, user, venda, produtos

app = Flask(__name__)
app.register_blueprint(loja.loja)
app.register_blueprint(user.user)
app.register_blueprint(venda.venda)
app.register_blueprint(produtos.produtos)

@app.route('/')
def index():
    return ''

@app.errorhandler(404)
def rotaNaoEncontrada(Erro):
    return "Rota não Encontrada" + str(Erro)

@app.errorhandler(403)
def erroDePermissao(Erro):
    return "Não tem permissão" + str(Erro)