from flask import Blueprint, request, jsonify
from data_processor import DataProcessor
from database_manager import DatabaseManager
from config import Config
import json

song_blueprint = Blueprint('songs',__name__)
db_manager = DatabaseManager(Config.DATABASE_URI)

def init_db(file_path):
    try:
        with open(file_path) as f:
            json_data = json.load(f)
        print(len(json_data))
        processor = DataProcessor(json_data)
        processor.normalize()
        db_manager.initialize_db(processor.df)
        print("Database initialized Successfully")
    except Exception as e:
        print(f"Error initializing database: {e}")

init_db(Config.JSON_FILE)

@song_blueprint.route('/songs',methods=['GET'])
def get_all_songs():
    try:
        page = request.args.get('page',1,type=int)
        per_page = request.args.get('per_page',10,type=int)
        result = db_manager.get_all_songs(page,per_page)
        total_items = result['total_items']
        songs = result['songs']
        total_pages = (total_items + per_page - 1) // per_page
        response = {
            'current_page' : page,
            'total_pages': total_pages,
            'items_per_page': per_page,
            'songs':songs
        }
        return jsonify(response)
    except Exception as e:
        return jsonify({'message': f'Error retrieving songs: {e}'}), 500

@song_blueprint.route('/song',methods=['GET'])
def get_song_by_title():
    try:
        title = request.args.get('title')
        song = db_manager.get_song_by_title(title)
        if song:
            return jsonify(song)
        else:
            return jsonify({'error': 'Song not found'}), 404
    except Exception as e:
        return jsonify({'message': f'Error retrievning song: {e}'}), 500
    

@song_blueprint.route('/rate',methods=['POST'])
def rate_song():
    try:
        data = request.json
        title = data.get('title')
        rating = data.get('rating')
        if rating < 0 or rating > 5 :
            return jsonify({'error' : ' Rating must between 0 and 5'}), 400
        rowcount = db_manager.rate_song(title, rating)
        if rowcount == 0:
            return jsonify({'error': 'Song not found'}), 404
        else:
            return jsonify({'message': 'Rating updated successfully'})
    except Exception as e:
        return jsonify({'message': f'Error rating song: {e}'}), 500
