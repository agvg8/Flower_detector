from ultralytics import YOLO

# 🔹 Ścieżka do wytrenowanego modelu (upewnij się, że to poprawna)
model = YOLO("runs/detect/train8/weights/best.pt")

# 🔹 Folder z klatkami (które wcześniej wyciągnęłaś z filmiku)
source_folder = "DATA/test_frames"

# 🔹 Uruchomienie detekcji
results = model.predict(
    source=source_folder,
    imgsz=640,
    conf=0.3,  # próg pewności (możesz np. zwiększyć na 0.5 jeśli masz dużo fałszywych detekcji)
    save=True  # zapisze obrazy z zaznaczonymi ramkami
)

print("Detekcja zakończona! Wyniki znajdziesz w folderze: runs/detect/predict")
