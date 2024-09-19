import datetime
import os

from ultralytics import YOLO
import cv2


class MachineLearning:

    @classmethod
    def learn(cls):
        model = YOLO('yolov8s.pt')
        file_data = """
        path: pothole_dataset_v8/
        train: 'train/images'
        val: 'valid/images'

        # class names
        names:
          0: 'pothole'
        """
        filename = "pothole_v8.yaml"
        my_file = open(filename, 'w')
        my_file.write(file_data)
        my_file.close()
        results = model.train(
            data='pothole_v8.yaml',
            imgsz=640,
            epochs=1,
            batch=16,
            name='yolov8n_custom')
        return results

    @classmethod
    def launch(cls, frame: cv2.typing.MatLike):
        model = YOLO('yolov8s.pt')
        path: str = os.getcwd() + "/temp/" + datetime.datetime.now().__str__() + ".jpg"
        cv2.imwrite(path, frame)
        results = model.predict(source=path, show=True, imgsz=100, show_labels=True, save=True, conf=0.1,)
        img = cv2.imread(path)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        image: cv2.UMat = cv2.UMat()
        for r in results[0]:
            for box in r.boxes:
                b = box.xyxy[0]
                start_point = (int(b[0]), int(b[1]))
                end_point = (int(b[2]), int(b[3]))
                color = (255, 0, 0)
                thickness = 2
                image = cv2.rectangle(img, start_point, end_point, color, thickness)
                print(b)
        try:
            cv2.imshow("frame", image)
        except cv2.error as e:
            pass
        return 0
