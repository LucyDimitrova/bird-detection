from pathlib import Path
import sqlite3
import pandas as pd

Path('database.db').touch()

conn = sqlite3.connect('database.db')
c = conn.cursor()

c.execute('''CREATE TABLE detections (Class text, Timestamp text, Frame int, BoundingBox_Coordinate_0 real, 
BoundingBox_Coordinate_1 real, BoundingBox_Coordinate_2 real, BoundingBox_Coordinate_3 real, Confidence real)''')

detections = pd.read_csv('files/output.csv')
detections.to_sql('detections', conn, if_exists='append', index = False)

print(c.execute('''SELECT * FROM detections''').fetchall())

