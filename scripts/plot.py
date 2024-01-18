import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

conn = sqlite3.connect('database.db')
c = conn.cursor()

print(len(c.execute('''SELECT * FROM detections WHERE Class = "bird"''').fetchall()))

df = pd.read_sql('select count(*) as birds, Timestamp, Frame from detections where Class = "bird" group by Timestamp', conn)
df.plot(x='Timestamp', y='birds')
plt.xlabel('Duration video (seconds)')
plt.ylabel('Number of birds detected')
plt.show()