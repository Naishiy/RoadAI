from datetime import datetime

import RoadRecognition
from src import MachineLearning
import os
import cv2


class Application:

    @classmethod
    def main(cls, use_camera: bool = False) -> None:
        source_path: str = '/Users/j/Documents/GitHub/RoadAI/resources/'
        destination_path: str = '/Users/j/Documents/GitHub/RoadAI/results/'
        if use_camera:
            cls.execute_camera()
        else:
            cls.convert_images(source_path, destination_path)
            try:
                image: cv2.typing.MatLike = RoadRecognition.ImageProcessor.image_to_frame(destination_path)
                cv2.imshow("dst", image)
                input("Enter to continue...")
            except FileNotFoundError:
                return
        return

    @classmethod
    def execute_camera(cls) -> None:
        capture_instance: cv2.VideoCapture = cv2.VideoCapture(0)
        while True:
            success, frame = capture_instance.read()
            if not success:
                break
            MachineLearning.launch(frame)
            if cls.is_required_quit():
                break
        capture_instance.release()
        cv2.destroyAllWindows()

    @classmethod
    def is_required_quit(cls) -> bool:
        return cv2.waitKey(1) & 0xFF == ord('q')

    @classmethod
    def convert_images(cls, source_path: str, destination_path: str) -> None:
        for file in os.listdir(source_path):
            destination_file: str = destination_path + file
            MachineLearning.launch(source_path + file)
            input()
        return


if __name__ == "__main__":
    Application.main(True)
