import cv2

from enums import ApplicationArguments
from models import *


class Application:
    __camera_index: int = 0

    @classmethod
    def main(cls, args: dict[ApplicationArguments] = None) -> None:
        capture_instance: cv2.VideoCapture = RoadRecognition.prepare_capture(
            args[ApplicationArguments.CAMERA_INDEX]
            if args is not None else Application.__camera_index)
        while True:
            success, frame = capture_instance.read()
            if not success:
                break
            RoadRecognition.execute_frame(success, frame)
            if cls.is_required_quit():
                break
        capture_instance.release()
        cv2.destroyAllWindows()

    @classmethod
    def is_required_quit(cls) -> bool:
        return cv2.waitKey(1) & 0xFF == ord('q')
