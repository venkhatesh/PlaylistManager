from flask import Flask, request, jsonify
from routes.song_routes import song_blueprint
from config import Config
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
app.config.from_object(Config)
app.register_blueprint(song_blueprint)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
