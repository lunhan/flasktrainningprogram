from flask import *
from Backend.adminGUI.adminGUI import admin

app = Flask(__name__)

app.register_blueprint(admin)

if __name__ == '__main__':
    app.run()
