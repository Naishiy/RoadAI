from ultralytics import YOLO
import cv2


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
myfile = open(filename, 'w')
myfile.write(file_data)
myfile.close()

# Запуск обучения
results = model.train(
    data='pothole_v8.yaml',
    imgsz=640,
    epochs=1,
    batch=16,
    name='yolov8n_custom')

# Тест
path = 'C:/Users/NIKITA/Documents/RoadAI/Easy1.jpg'
results = model([path])

# OpenCV для визуализации
img = cv2.imread(path)
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
