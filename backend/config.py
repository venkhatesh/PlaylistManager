import os
import logging

class Config:
    DEBUG = True
    DATABASE_URI = 'sqlite:///../database/songs.db'
    JSON_FILE = 'database/playlist.json'

    LOGGING_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    LOGGING_LOCATION = 'logs/playlistmanager.log'
    LOGGING_LEVEL = logging.DEBUG

    @staticmethod
    def configure_logging():
        if not os.path.exists(os.path.dirname(Config.LOGGING_LOCATION)):
            os.makedirs(os.path.dirname(Config.LOGGING_LOCATION))

        logging.basicConfig(
            filename=Config.LOGGING_LOCATION,
            level=Config.LOGGING_LEVEL,
            format=Config.LOGGING_FORMAT
        )

Config.configure_logging()