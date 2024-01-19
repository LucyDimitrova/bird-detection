import json
from pathlib import Path
import pandas as pd
from ultralytics import YOLO

# Input/output paths
FRAMES_PATH = 'files/frames/'
OUTPUT_PATH = 'files/output.csv'
OUTPUT_COLUMNS = ['Class', 'Timestamp', 'Frame', 'BoundingBox_Coordinate_0', 'BoundingBox_Coordinate_1',
                  'BoundingBox_Coordinate_2', 'BoundingBox_Coordinate_3', 'Confidence']


def detect(frames_path=FRAMES_PATH, output_path=OUTPUT_PATH, output_header=OUTPUT_COLUMNS):
    """Performs object detection on a directory of frames

    :param frames_path: path to frames directory
    :param output_path: path to output csv file
    :return:
    """
    # Create an empty dataframe
    df = pd.DataFrame(columns=output_header)

    try:
        # Load pre-trained model
        model = YOLO('yolov8n.pt')

        # Perform detection on the frames
        results = model.predict(source=frames_path)

        # Process the result for each frame
        for result in results:
            try:
                frame_name = Path(result.path).name
                frame_details = frame_name.split('_')
                frame = frame_details[0]
                timestamp = frame_details[1]
                detections = json.loads(result.tojson())

                # Generate rows for each detection
                data = [
                    {
                        'Class': detection['name'],
                        'Timestamp': timestamp,
                        'Frame': frame,
                        'BoundingBox_Coordinate_0': detection['box']['x1'],
                        'BoundingBox_Coordinate_1': detection['box']['y1'],
                        'BoundingBox_Coordinate_2': detection['box']['x2'],
                        'BoundingBox_Coordinate_3': detection['box']['y2'],
                        'Confidence': detection['confidence'],
                     } for detection in detections
                ]

                # Add rows to dataframe
                df = pd.concat([df, pd.DataFrame(data)], ignore_index=True)
            except:
                print(f'Error processing detections in frame {result.path}')
                continue
    except:
        print('Error generating object detections')
    finally:
        # Save to csv
        df.to_csv(output_path, index=False)


if __name__ == '__main__':
    detect()
