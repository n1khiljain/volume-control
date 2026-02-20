import cv2

HAND_CONNECTIONS = [
    (0, 1), (1, 2), (2, 3), (3, 4),        # Thumb
    (0, 5), (5, 6), (6, 7), (7, 8),        # Index finger
    (0, 9), (9, 10), (10, 11), (11, 12),   # Middle finger
    (0, 13), (13, 14), (14, 15), (15, 16), # Ring finger
    (0, 17), (17, 18), (18, 19), (19, 20), # Pinky
    (5, 9), (9, 13), (13, 17)              # Palm
]

def draw_hand_landmarks(frame, hand_landmarks):
    """Draw landmarks and connections on frame."""
    h, w, _ = frame.shape
    
    # Draw landmark points
    for landmark in hand_landmarks:
        x, y = int(landmark.x * w), int(landmark.y * h)
        cv2.circle(frame, (x, y), 10, (0, 255, 0), -1)
    
    # Draw connections
    for start_idx, end_idx in HAND_CONNECTIONS:
        x1, y1 = int(hand_landmarks[start_idx].x * w), int(hand_landmarks[start_idx].y * h)
        x2, y2 = int(hand_landmarks[end_idx].x * w), int(hand_landmarks[end_idx].y * h)
        cv2.line(frame, (x1, y1), (x2, y2), (255, 0, 0), 5)
