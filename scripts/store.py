from pathlib import Path
import sqlite3
import pandas as pd

DATABASE_NAME = 'database.db'
INPUT_PATH = 'files/output.csv'


def store_data_from_csv(db_name=DATABASE_NAME, input_file=INPUT_PATH):
    """Reads data from csv file into an sqlite database

    :param db_name: empty database name
    :param input_file: path to csv file
    :return:
    """
    # Create empty sqlite database file
    Path(db_name).touch()

    # Create connection to db
    conn = sqlite3.connect(db_name)
    c = conn.cursor()

    try:
        # Create detections table
        create_table_query = '''CREATE TABLE detections (Class text, Timestamp text, Frame int, BoundingBox_Coordinate_0 
        real, BoundingBox_Coordinate_1 real, BoundingBox_Coordinate_2 real, BoundingBox_Coordinate_3 real, Confidence 
        real)'''
        c.execute(create_table_query)
    except:
        print('Error creating detections table in sqlite')

    try:
        # Read data from csv file and insert into db
        detections = pd.read_csv(input_file)
        detections.to_sql('detections', conn, if_exists='append', index=False)
    except:
        print('Error reading/inserting data into sqlite')


if __name__ == '__main__':
    store_data_from_csv()
