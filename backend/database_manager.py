import sqlite3

class DatabaseManager:

    def __init__(self, db_path='database/database.db',table_name='songs'):
        self.db_path = db_path
        self.table_name = table_name

    def initialize_db(self,df,db_name='songs'):
        df = df.astype(str)
        conn = sqlite3.connect(self.db_path)
        df.to_sql(self.table_name,conn,if_exists='replace',index=False)
        conn.close()

    def get_all_songs(self,page,per_page):
        offset = (page-1) * per_page
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute(f"SELECT COUNT(*) FROM {self.table_name}")
        total_items = cursor.fetchone()[0]
        cursor.execute(f"SELECT * FROM {self.table_name} LIMIT {per_page} OFFSET {offset}")
        songs = cursor.fetchall()
        col_names = [desc[0] for desc in cursor.description]
        conn.close()
        return {
            'total_items' : total_items,
            'songs' : [dict(zip(col_names, song)) for song in songs]
        }
    
    def get_song_by_title(self,title):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM {self.table_name} WHERE title = ?",(title,))
        song = cursor.fetchone()
        conn.close()
        if song:
            col_names = [desc[0] for desc in cursor.description]
            return dict(zip(col_names,song))
        return None
    
    def rate_song(self,title,rating):
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute(f"UPDATE {self.table_name} SET star_rating = ? WHERE title = ?", (rating,title))
        conn.commit()
        rowcount = cursor.rowcount
        conn.close()
        return rowcount
