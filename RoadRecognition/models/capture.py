import cv2


class Capture(cv2.VideoCapture):

    def __init__(self, camera_index: int) -> None:
        super().__init__(camera_index)

    def isOpened(self) -> bool:
        is_opened: bool = super().isOpened()
        if not is_opened:
            print("Camera doesn't work.")
        return is_opened
