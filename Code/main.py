from operator import truediv

from ultralytics import YOLO
import cv2


def Learn():
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


def launch_machine(source_path: str, destination_path: str):
    model = YOLO('yolov8s.pt')
    results = model.predict(
        source=source_path,
        show=True,
        imgsz=100,
        hide_labels=True,
        save=True,
        name=destination_path,
        conf=0.1,
    )

    img = cv2.imread(source_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    for r in results[0]:
        for box in r.boxes:
            b = box.xyxy[0]
            c = box.cls
            start_point = (int(b[0]), int(b[1]))
            end_point = (int(b[2]), int(b[3]))
            color = (255, 0, 0)
            thickness = 2
            image = cv2.rectangle(img, start_point, end_point, color, thickness)
            print(b)
    cv2.imshow("frame", image)
    return 0

#Test('Easy1.jpg')
Learn()
