import cv2


class ImageProcessor:
    @staticmethod
    def image_to_frame(image_path: str) -> cv2.typing.MatLike:
        image = cv2.imread(image_path)
        if image is None:
            raise FileNotFoundError
        return image

