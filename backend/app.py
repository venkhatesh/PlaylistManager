from flask import Flask, request, jsonify
from routes.song_routes import song_blueprint
from config import Config
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
app.config.from_object(Config)
app.register_blueprint(song_blueprint)

# DATABASE = 'database/songs.db'
# db_manager = DatabaseManager(db_path=DATABASE)

# #method to fill db from json file
# def init_db(file_path):
#     with open(file_path) as f:
#         json_data = json.load(f)
#     print(len(json_data))
#     processor = DataProcessor(json_data)
#     processor.normalize()
#     db_manager.initialize_db(processor.df)
#     print("Database initialized Successfully")

# #endpoint to fill the db with custom json file
# @app.route('/initdb', methods=['POST'])
# def init_db_route():
#     if 'file' not in request.files:
#         return jsonify({'error' : 'No file part in the request'}), 400
#     file = request.files['file']
#     if file.filename == '':
#         return jsonify({'error' : 'No file selected'}), 400
#     if file and file.filename.endswith('.json'):
#         file_path = "database/" + file.filename
#         file.save(file_path)
#     init_db(file_path)
#     return jsonify({'message' : ' Database initialized successfully'})

# #endpoint to get all songs with pagination
# @app.route('/songs',methods=['GET'])
# def get_all_songs():
#     page = request.args.get('page',1,type=int)
#     per_page = request.args.get('per_page',10,type=int)
#     result = db_manager.get_all_songs(page,per_page)
#     total_items = result['total_items']
#     songs = result['songs']
#     total_pages = (total_items + per_page - 1) // per_page
#     response = {
#         'current_page' : page,
#         'total_pages': total_pages,
#         'items_per_page': per_page,
#         'songs':songs
#     }
#     return jsonify(response)

# #endpoint to get song by title
# @app.route('/song',methods=['GET'])
# def get_song_byt_title():
#     title = request.args.get('title')
#     song = db_manager.get_song_by_title(title)
#     if song:
#         return jsonify(song)
#     else:
#         return jsonify({'error': 'Song not found'}), 404
    
#  #endpoint to rate the song   
# @app.route('/rate',methods=['POST'])
# def rate_song():
#     data = request.json
#     title = data.get('title')
#     rating = data.get('rating')
#     if rating < 0 or rating > 5 :
#         return jsonify({'error' : ' Rating must between 0 and 5'}), 400
#     rowcount = db_manager.rate_song(title, rating)
#     if rowcount == 0:
#         return jsonify({'error': 'Song not found'}), 404
#     else:
#         return jsonify({'message': 'Rating updated successfully'})

if __name__ == '__main__':
    # init_db('database/playlist.json')
    app.run(host='0.0.0.0', port=5000)
