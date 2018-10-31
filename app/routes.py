from flask import render_template
from app import app
import oci_setup as ocis


@app.route('/')
@app.route('/index')
def index():
    user = {'username':'Kevin'}
    list_all = {'services': ocis.print_resources()}
    return render_template('index.html', title='Home', user=user, list_all=list_all)

