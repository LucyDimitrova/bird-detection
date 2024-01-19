import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

DATABASE_NAME = 'database.db'
PLOT_PATH = 'files/plot.png'


def plot_bird_frequency(storage=DATABASE_NAME, plot=PLOT_PATH):
    """Creates a plot with bird frequency in time

    :param storage: name of sqlite db
    :param plot: path to output plot file
    :return:
    """
    try:
        # Connect to database
        conn = sqlite3.connect(storage)

        # Perform filter query and read into dataframe
        filter_query = ('select count(*) as birds, Timestamp, Frame from detections where Class = "bird" group by '
                        'Timestamp')
        df = pd.read_sql(filter_query, conn)

        try:
            # Create plot
            df.plot(x='Timestamp', y='birds', figsize=(12.8, 9.6))
            plt.xlabel('Duration video (seconds)')
            plt.ylabel('Number of birds detected')
            plt.savefig(plot)
        except:
            print('Error creating plot')
    except:
        print('Error reading data from db')


if __name__ == '__main__':
    plot_bird_frequency()
