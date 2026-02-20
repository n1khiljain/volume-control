import math

def get_distance(p1,p2,w,h):
    x1, y1 = p1.x * w, p1.y * h
    x2, y2 = p2.x * w, p2.y * h
    distance = math.hypot(x2-x1, y2-y1)
    print(distance)
    return distance

def get_pinch_ratio(hand_landmarks, w, h):
    pinch_dist = get_distance(hand_landmarks[4], hand_landmarks[8], w, h)

    # using wrist to middle finger as reference point
    ref_dist = get_distance(hand_landmarks[0], hand_landmarks[12], w, h)

    return pinch_dist / ref_dist if ref_dist > 0 else 0