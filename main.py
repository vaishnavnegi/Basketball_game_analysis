from ultralytics import YOLO
model = YOLO("yolov8x.pt")  # Load a pretrained model (or specify a custom path)
results = model.predict("input_videos/video_1.mp4", save=True)  # Predict on webcam (or specify a custom video path)
print(results)  # Print results to console
print("=======================")
for box in results[0].boxes:
    print(f"Box coordinates: {box.xyxy}")  # Print box coordinates
    print(f"Box confidence: {box.conf}")  # Print box confidence
    print(f"Box class: {box.cls}")  # Print box class
    print("=======================")