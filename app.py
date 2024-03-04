# app.py

from flask import Flask
from flask_cors import CORS
from routes import router

app = Flask(__name__)
CORS(app)

# separate these routes
app.register_blueprint(router)

if __name__ == '__main__':
    app.run(debug=True)
