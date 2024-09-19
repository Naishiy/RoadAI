import datetime
import time

import cv2

from src import MachineLearning
from RoadRecognition import ImageProcessor

class Application:
    __camera_index: int = 0

    @classmethod
    def main(cls, source_path: str, destination_path: str) -> None:
        capture_instance: cv2.VideoCapture = cv2.VideoCapture(0)
        while True:
            success, frame = capture_instance.read()
            if not success:
                break
            filename = datetime.datetime.now().__str__()
            source_file: str = source_path + filename
            destination_file: str = destination_path + filename
            cv2.imwrite(source_file, frame)
            MachineLearning.launch(source_file)
            ImageProcessor.image_to_frame(destination_path)
            cv2.imshow('Video', frame)
            time.sleep(1)
            if cls.is_required_quit():
                break
        capture_instance.release()
        cv2.destroyAllWindows()

    @classmethod
    def is_required_quit(cls) -> bool:
        return cv2.waitKey(1) & 0xFF == ord('q')
