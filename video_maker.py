import cv2
import os

frames_folder = "runs/detect/predict"
output_video = "runs/detect/predict_video.avi"

frames = sorted([f for f in os.listdir(frames_folder) if f.endswith(".jpg")])
if not frames:
    print("Brak klatek!")
    exit()

first_frame = cv2.imread(os.path.join(frames_folder, frames[0]))
h, w, _ = first_frame.shape
fourcc = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter(output_video, fourcc, 10, (w, h))

for f in frames:
    frame = cv2.imread(os.path.join(frames_folder, f))
    out.write(frame)

out.release()
print("Film zapisany jako:", output_video)
