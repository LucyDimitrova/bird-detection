from scripts.extract_frames import extract_frames
from scripts.detect import detect
from scripts.store import store_data_from_csv
from scripts.plot import plot_bird_frequency

INPUT_PATH = 'input/Pigeon - 6093.mp4'
FRAMES_DIR = 'files/frames/'
CSV_PATH = 'files/output.csv'
OUTPUT_COLUMNS = ['Class', 'Timestamp', 'Frame', 'BoundingBox_Coordinate_0', 'BoundingBox_Coordinate_1',
                  'BoundingBox_Coordinate_2', 'BoundingBox_Coordinate_3', 'Confidence']
DATABASE_NAME = 'database.db'
PLOT_PATH = 'files/plot.png'


def run():
    extract_frames(INPUT_PATH, FRAMES_DIR)
    detect(FRAMES_DIR, CSV_PATH, OUTPUT_COLUMNS)
    store_data_from_csv(DATABASE_NAME, CSV_PATH)
    plot_bird_frequency(DATABASE_NAME, PLOT_PATH)


if __name__ == '__main__':
    run()
