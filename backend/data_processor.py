import pandas as pd
import sqlite3 

class DataProcessor:
    def __init__(self, json_data):
        self.data = json_data
        self.df = pd.DataFrame(self.data)
        self.df['star_rating']=0
        self.normalized_df = None
    
    def normalize(self):
        self.df.reset_index(inplace=True)
        self.df.rename(columns={'index':'index'},inplace=True)
        columns_order = ['index'] + list(self.df.columns.drop('index'))
        self.normalized_df = self.df[columns_order]
        return self.normalized_df
    
