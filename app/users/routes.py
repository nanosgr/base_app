from flask import Blueprint

users = Blueprint('users', __name__)

@users.route('/route_name', methods=['GET', 'POST'])
def method_name():
   pass