import json
from pathlib import Path
import pandas as pd
from ultralytics import YOLO

# Load pre-trained model
model = YOLO("yolov8n.pt")

# Frames path
frames_path = "files/frames"

# Create empty dataframe
OUTPUT_COLUMNS = ['Class', 'Timestamp', 'Frame', 'BoundingBox_Coordinate_0', 'BoundingBox_Coordinate_1', 'BoundingBox_Coordinate_2', 'BoundingBox_Coordinate_3', 'Confidence']
df = pd.DataFrame(columns=OUTPUT_COLUMNS)

# Predict
results = model.predict(source=frames_path)

for result in results:
    frame_name = Path(result.path).name
    frame_details = frame_name.split('_')
    frame = frame_details[0]
    timestamp = frame_details[1]
    detections = json.loads(result.tojson())
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
    df = pd.concat([df, pd.DataFrame(data)], ignore_index=True)

df.to_csv('files/output.csv', index=False)


