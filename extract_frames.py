import cv2
import os

# Ścieżka do filmiku
video_path = "DATA/test_video/video.mp4"
output_folder = "DATA/test_frames"

# Utworzenie folderu jeśli nie istnieje
os.makedirs(output_folder, exist_ok=True)

# Wczytanie filmiku
cap = cv2.VideoCapture(video_path)

frame_rate = 5  # liczba klatek na sekundę do zapisania
frame_id = 0
count = 0

fps = cap.get(cv2.CAP_PROP_FPS)
interval = int(fps / frame_rate)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    if count % interval == 0:
        frame_name = os.path.join(output_folder, f"frame_{frame_id:04d}.jpg")
        cv2.imwrite(frame_name, frame)
        print("Zapisano:", frame_name)
        frame_id += 1
    count += 1

cap.release()
print("Gotowe — zapisano wszystkie klatki do", output_folder)
