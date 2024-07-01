from flask import Blueprint, request, jsonify
from data_processor import DataProcessor
from database_manager import DatabaseManager
from config import Config
import json
import logging

logger = logging.getLogger(__name__)
song_blueprint = Blueprint('songs',__name__)
db_manager = DatabaseManager(Config.DATABASE_URI)

def init_db(file_path):
    logger.info("Initializing database")
    try:
        with open(file_path) as f:
            json_data = json.load(f)
        print(len(json_data))
        processor = DataProcessor(json_data)
        processor.normalize()
        db_manager.initialize_db(processor.df)
        logger.info("Database initialized Successfully")
    except Exception as e:
        logger.error(f"Error initializing database: {e}")


@song_blueprint.route('/initdb', methods=['POST'])
def init_db_route():
    if 'file' not in request.files:
        return jsonify({'error' : 'No file part in the request'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error' : 'No file selected'}), 400
    if file and file.filename.endswith('.json'):
        file_path = "database/" + file.filename
        file.save(file_path)
    init_db(file_path)
    return jsonify({'message' : ' Database initialized successfully'})

init_db(Config.JSON_FILE)

@song_blueprint.route('/songs',methods=['GET'])
def get_all_songs():
    logger.info("Fetching all songs")
    try:
        page = request.args.get('page',1,type=int)
        per_page = request.args.get('per_page',10,type=int)
        result = db_manager.get_all_songs(page,per_page)
        logger.info("Songs fetched successfully")
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
        logger.error(f"Error fetching songs: {e}")
        return jsonify({'message': f'Error retrieving songs: {e}'}), 500

@song_blueprint.route('/song',methods=['GET'])
def get_song_by_title():
    logger.info("Fetching song by title")
    try:
        title = request.args.get('title')
        song = db_manager.get_song_by_title(title)
        if song:
            logger.info(f"Song '{title}' fetched successfully")
            return jsonify(song)
        else:
            logger.warning(f"Song '{title}' not found")
            return jsonify({'error': 'Song not found'}), 404
    except Exception as e:
        logger.error(f"Error fetching song by title : {e}")
        return jsonify({'message': f'Error retrieving song: {e}'}), 500
    

@song_blueprint.route('/rate',methods=['POST'])
def rate_song():
    logger.info("Rating song")
    try:
        data = request.json
        title = data.get('title')
        rating = data.get('rating')
        if rating < 0 or rating > 5 :
            return jsonify({'error' : ' Rating must between 0 and 5'}), 400
        rowcount = db_manager.rate_song(title, rating)
        if rowcount == 0:
            logger.warning(f"Song '{title}' not found for rating")
            return jsonify({'error': 'Song not found'}), 404
        else:
            logger.info(f"Rating for song'{title}' updated to {rating}")
            return jsonify({'message': 'Rating updated successfully'})
    except Exception as e:
        logger.error(f"Error rating song: {e}")
        return jsonify({'message': f'Error rating song: {e}'}), 500
