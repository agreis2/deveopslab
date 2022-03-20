from flask import Flask

from flask_wtf.csrf import CSRFProtect
import os

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return "Hello World- Ana Reis test"

if __name__ == '__main__':
    port = os.getenv('PORT')
    app.run('0.0.0.0', port=port)
