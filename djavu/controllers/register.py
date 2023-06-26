import functools

from quart import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, jsonify
)
from werkzeug.security import check_password_hash, generate_password_hash

from djavu.db import get_db
from djavu.repository import userRepository

bp = Blueprint('register', __name__, url_prefix='/')

repo = userRepository()

@bp.route('/users')
def users():
    users = repo.list_users()
    return jsonify(users)
    #return jsonify(render_template('users.html', users=users))
