from flask import *

admin = Blueprint('admin', __name__)

@admin.route('/partner')
def partner():
    return render_template('partner.html')

@admin.route('/members')
def members():
    return render_template('members.html')

@admin.route('/event')
def event():
    return render_template('event.html')

