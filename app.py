from flask import Flask
from ferrari import ferrari

app = Flask(__name__)
app.register_blueprint(ferrari, url_prefix="/")

if __name__ == '__main__':
    app.run(debug=True, port=8000)