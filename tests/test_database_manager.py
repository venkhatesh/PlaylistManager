import unittest
import sqlite3
import pandas as pd
from backend.database_manager import DatabaseManager

class TestDatabaseManager(unittest.TestCase):

    def setUp(self):
        self.test_db_path = 'database/test_songs.db'
        self.db_manager = DatabaseManager(db_path=self.test_db_path, table_name='test_songs')
        self.test_data = pd.DataFrame({
            'title':['Song1','Song2'],
            'danceability':[0.8,0.9],
            'energy':[0.6,0.7],
            'tempo':[120,130],
            'star_rating':[4,5]
        })
        self.db_manager.initialize_db(self.test_data)


    def test_initialize_db(self):
        with sqlite3.connect(self.test_db_path) as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='test_songs'")
            self.assertIsNotNone(cursor.fetchone())

    def test_get_all_songs(self):
        result = self.db_manager.get_all_songs(1,2)
        songs = result['songs']
        self.assertEqual(result['total_items'],2)
        self.assertEqual(len(songs),2)
        self.assertEqual(songs[0]['title'],'Song1')

    def test_get_song_by_title(self):
        song = self.db_manager.get_song_by_title('Song1')
        self.assertIsNotNone(song)
        self.assertEqual(song['title'],'Song1')

    def test_rate_song(self):
        self.db_manager.rate_song('Song1',3)
        song = self.db_manager.get_song_by_title('Song1')
        self.assertEqual(int(song['star_rating']),3)

if __name__ == '__main__':
    unittest.main(verbosity=2)

