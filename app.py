from flask import *
from page.page import page

app = Flask(__name__)

#TODO:
app.register_blueprint(page)

if __name__ == '__main__':
    app.run()
