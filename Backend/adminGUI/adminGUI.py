from flask import *

# TODO:创建一个蓝图
admin = Blueprint('admin', __name__)

# TODO:把partner page作为打开网页的default页面
@admin.route('/')
def partner():
    return render_template('partner.html')

# TODO:可以切换到members页面
@admin.route('/members')
def members():
    return render_template('members.html')

# TODO:可以切换到event页面
@admin.route('/event')
def event():
    return render_template('event.html')
