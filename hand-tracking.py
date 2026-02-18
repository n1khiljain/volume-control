import cv2
import mediapipe as mp
from mediapipe.tasks import python
from mediapipe.tasks.python import vision
import time

cap = cv2.VideoCapture(0)

MODEL_PATH = "/Users/nikhiljain/Desktop/Coding Projects/volume-control/Task.task"

BaseOptions = mp.tasks.BaseOptions
HandLandmarker = mp.tasks.vision.HandLandmarker
HandLandmarkerOptions = mp.tasks.vision.HandLandmarkerOptions
VisionRunningMode = mp.tasks.vision.RunningMode

options = HandLandmarkerOptions(
    base_options=BaseOptions(model_asset_path=MODEL_PATH),
    num_hands=2,
    running_mode=VisionRunningMode.VIDEO)

start_time = time.time()

with HandLandmarker.create_from_options(options) as landmarker:
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frame = cv2.flip(frame, 1)
        frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=frameRGB)

        frame_timestamp_ms = int((time.time() - start_time) * 1000)

        hand_landmarker_result = landmarker.detect_for_video(mp_image, frame_timestamp_ms)

        # Check if any hands were detected
        if hand_landmarker_result.hand_landmarks:
            num_hands = len(hand_landmarker_result.hand_landmarks)
            print(f"Hand Detected! Count: {num_hands}")
        else:
            print("No hand detected.")

        cv2.imshow("Frame", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()