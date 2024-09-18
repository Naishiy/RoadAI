from services import ImageProcessor
from models import RoadRecognition
import cv2


class DesktopApplication:

    __folder: str = '/Users/j/Downloads/'
    __file_path: str = __folder + "G0011937.jpg"

    @classmethod
    def main(cls, args: list[str] = None) -> None:
        frame = ImageProcessor.image_to_frame(cls.__file_path)
        processed_frame = RoadRecognition.frame_processor(frame)
        cv2.imshow('image', processed_frame)
        cv2.imwrite(cls.__folder + 'test.jpg', processed_frame)


if __name__ == "__main__":
    DesktopApplication.main()
