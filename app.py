from apiLoja import loja, user, venda, produtos, admin
from flask import Flask, g, session, render_template
from datetime import timedelta
import os

app = Flask(__name__)
app.register_blueprint(loja.loja)
app.register_blueprint(user.user)
app.register_blueprint(admin.admin)
app.register_blueprint(venda.venda)
app.register_blueprint(produtos.produtos)
app.secret_key = os.urandom(24)
app.permanent_session_lifetime = timedelta(hours=24)

@app.errorhandler(404)
def rotaNaoEncontrada(Erro):
    return render_template('notfound.html')

@app.errorhandler(403)
def erroDePermissao(Erro):
    return "Não tem permissão" + str(Erro)

@app.before_request
def before_request():
    g.username = None
    g.userid = None
    g.admin = None

    if 'username' in session:
        g.username = session['username']

    if 'userid' in session:
        g.userid = session['userid']

    if 'admin' in session:
        g.admin = session['admin']

@app.teardown_appcontext
def teardown(_exeption):
    ...