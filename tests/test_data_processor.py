import unittest
import json
import os
import sqlite3
import pandas as pd
from backend.database_manager import DatabaseManager
from backend.data_processor import DataProcessor

class TestDataProcessor(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.test_json_path = 'database/playlist_test.json'
        cls.test_db_path = 'database/test_songs.db'
        cls.test_data = {
           "id" : {"0":"5vYA1mW9g2Coh1HUFUSmlb","1":"2klCjJcucgGQysgH170npL"},
           "title" : {"0":"Song1","1":"Song2"}
        }
        with open(cls.test_json_path,'w') as f:
            json.dump(cls.test_data, f)

        with open(cls.test_json_path) as f:
            json_data = json.load(f)

        cls.processor = DataProcessor(json_data)
        cls.processor.normalize()

        cls.db_manager = DatabaseManager(db_path=cls.test_db_path, table_name='test_songs')
        cls.db_manager.initialize_db(cls.processor.df)

    @classmethod
    def tearDownClass(cls):
        os.remove(cls.test_json_path)

    def test_database_initialized(self):
        print("Running test_database_initialized")
        with sqlite3.connect(self.db_manager.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='test_songs'")
            self.assertIsNotNone(cursor.fetchone())
        print("test_database_initialized passed")

    def test_data_integrity(self):
        print("Running test_data_integrity")
        result = self.db_manager.get_all_songs(1,2)
        songs = result['songs']
        print("SONGs",songs)
        self.assertEqual(result['total_items'],2)
        self.assertEqual(len(songs),2)
        self.assertEqual(songs[0]['title'],'Song1')
        self.assertEqual(songs[1]['title'],'Song2')
        print("test_data_integrity passed")

if __name__ == '__main__':
    unittest.main()


