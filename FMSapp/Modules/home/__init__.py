from flask import Blueprint, render_template, request

viewhome = Blueprint('viewhome', __name__)


@viewhome.route('/index', methods=['GET'])
@viewhome.route('/',methods=['GET'])
def home():
    return render_template('Landing/welcome.html')
