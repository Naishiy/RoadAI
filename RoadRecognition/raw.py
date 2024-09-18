import cv2
import numpy as np
from tkinter import Tk, Label, Button, filedialog
from PIL import Image, ImageTk


class ImageApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Processor")
        self.load_button = Button(root, text="Load Image", command=self.load_image)
        self.load_button.pack()
        self.image_label = Label(root)
        self.image_label.pack()

    def load_image(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("Image files", "*.jpg *.jpeg *.png")]
        )
        if file_path:
            image = self.load_and_process_image(file_path)
            self.display_image(image)

    @staticmethod
    def load_and_process_image(file_path: str) -> np.ndarray:
        image = cv2.imread(file_path)
        if image is None:
            raise FileNotFoundError(f"Cannot load image at path: {file_path}")
        processed_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        return processed_image

    def display_image(self, image: np.ndarray):
        pil_image = Image.fromarray(image)
        tk_image = ImageTk.PhotoImage(image=pil_image)
        self.image_label.config(image=tk_image)
        self.image_label.image = tk_image


if __name__ == "__main__":
    root = Tk()
    app = ImageApp(root)
    root.mainloop()
