# En este archivo se agregan las rutas de la aplicacion
# Para lo cual el usuario no necesita estár logueado
# ver si es necesario agregar para éste modulo en particular
# el archivo para las clases de los formularios.

from flask import Blueprint
from flask.templating import render_template

main = Blueprint('main', __name__)


@main.route('/')
@main.route('/home')
@main.route('/index')
def home():
    return render_template('index.html')

@main.route('/about')
def about():
    pass