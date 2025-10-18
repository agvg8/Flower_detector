from ultralytics import YOLO

# użyj YOLOv8n (n = nano)
model = YOLO("yolov8n.pt")

# trenuj na swoich danych
model.train(data="DATA/data.yaml", epochs=20, imgsz=640)
