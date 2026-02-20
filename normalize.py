import math
from termios import VEOL

def get_distance(p1,p2,w,h):
    x1, y1 = p1.x * w, p1.y * h
    x2, y2 = p2.x * w, p2.y * h
    distance = math.hypot(x2-x1, y2-y1)
    return distance

def get_pinch_ratio(hand_landmarks, w, h):
    pinch_dist = get_distance(hand_landmarks[4], hand_landmarks[8], w, h)

    # using wrist to middle finger as reference point
    ref_dist = get_distance(hand_landmarks[0], hand_landmarks[12], w, h)

    ratio = pinch_dist / ref_dist if ref_dist > 0 else 0
    

    return ratio

def ratio_to_brightness(ratio, min_ratio=0.15, max_ratio=1.1):
    """
    Converts our pinch ratio to screen brightness (0-100)
    """
    # linear interpolation
    brightness = (ratio - min_ratio) / (max_ratio - min_ratio) * 100
    brightness = max(0, min(100, brightness))
    print(brightness)
    return brightness