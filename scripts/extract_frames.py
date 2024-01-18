import cv2 as cv

input_path = 'input/Pigeon - 6093.mp4'
capture = cv.VideoCapture(input_path)

count = 0
success, image = capture.read()
while success:
    count += 1

    # Get the current frame timestamp in milliseconds
    timestamp_msec = capture.get(cv.CAP_PROP_POS_MSEC)

    # Convert the timestamp to minutes, seconds, and milliseconds
    minutes = int((timestamp_msec % (1000 * 60 * 60)) / (1000 * 60))
    seconds = int((timestamp_msec % (1000 * 60)) / 1000)
    milliseconds = int(timestamp_msec % 1000)

    # Create the formatted timestamp string
    timestamp = f'{minutes:02d}:{seconds:02d}:{milliseconds:03d}'

    cv.imwrite(f'files/frame1/{count}_{timestamp}_frame.jpg', image)
    success, image = capture.read()

print(f'Extracted {count} frames from video')

capture.release()
cv.destroyAllWindows()
