# En este archivo se agregan las rutas de la aplicacion
# Para lo cual el usuario no necesita estár logueado
# ver si es necesario agregar para éste modulo en particular
# el archivo para las clases de los formularios.

from flask import Blueprint
from flask.templating import render_template

main = Blueprint('main', __name__)


@main.route('/')
@main.route('/home')
def home():
    return render_template('home.html')

@main.route('/about')
def about():
    pass