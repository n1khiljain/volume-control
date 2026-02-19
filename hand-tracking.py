import cv2
import mediapipe as mp
import time
from draw_utils import draw_hand_landmarks
import math

# Setup
MODEL_PATH = "Task.task"
cap = cv2.VideoCapture(0)

options = mp.tasks.vision.HandLandmarkerOptions(
    base_options=mp.tasks.BaseOptions(model_asset_path=MODEL_PATH),
    num_hands=2,
    running_mode=mp.tasks.vision.RunningMode.VIDEO)

start_time = time.time()

with mp.tasks.vision.HandLandmarker.create_from_options(options) as landmarker:
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        frame = cv2.flip(frame, 1)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        mp_image = mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb_frame)
        
        timestamp_ms = int((time.time() - start_time) * 1000)
        result = landmarker.detect_for_video(mp_image, timestamp_ms)
        
        # Draw landmarks for each detected hand
        for hand_landmarks in result.hand_landmarks:
            thumb_tip = hand_landmarks[4]
            index_tip = hand_landmarks[8]

            h, w, _ = frame.shape
            thumb_pos = (int(thumb_tip.x * w), int(thumb_tip.y * h))
            index_pos = (int(index_tip.x * w), int(index_tip.y * h))

            distance = math.hypot(index_pos[0] - thumb_pos[0], index_pos[1] - thumb_pos[1])
            print(distance)

            draw_hand_landmarks(frame, hand_landmarks)
        
        cv2.imshow("Hand Tracking", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
