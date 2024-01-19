import cv2 as cv

INPUT_PATH = 'input/Pigeon - 6093.mp4'
OUTPUT_PATH = 'files/frames/'


def extract_frames(input_path=INPUT_PATH, output_path=OUTPUT_PATH):
    """ Extracts frames from a video file

    :param input_path: path to video
    :param output_path: path to frames directory
    :return:
    """
    try:
        capture = cv.VideoCapture(input_path)

        count = 0
        while True:
            try:
                count += 1
                success, image = capture.read()

                # No more frames
                if not success:
                    print(f'Extracted {count - 1} frames from video')
                    break
                else:
                    # Get the current frame timestamp in milliseconds
                    timestamp_msec = capture.get(cv.CAP_PROP_POS_MSEC)

                    # Convert the timestamp to minutes, seconds and milliseconds
                    minutes = int((timestamp_msec % (1000 * 60 * 60)) / (1000 * 60))
                    seconds = int((timestamp_msec % (1000 * 60)) / 1000)
                    milliseconds = int(timestamp_msec % 1000)

                    # Create the formatted timestamp string
                    timestamp = f'{minutes:02d}:{seconds:02d}:{milliseconds:03d}'

                    cv.imwrite(f'{output_path}{count}_{timestamp}_frame.jpg', image)
            except:
                print(f'Error occurred while processing frame #{count}')
                continue

        capture.release()
    except:
        print('Error occurred while creating capture')
    finally:
        cv.destroyAllWindows()


if __name__ == '__main__':
    extract_frames()
