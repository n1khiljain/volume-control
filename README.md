# Hand Gesture Volume Control

Control your system volume using hand gestures detected via webcam.

## How It Works

Uses MediaPipe's Hand Landmarker to detect 21 hand landmarks in real-time from your webcam feed. The distance between your thumb and index finger controls the volume level.

## Setup

1. **Create virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Download the Hand Landmarker model**
   
   Download `hand_landmarker.task` from [Google AI Edge](https://ai.google.dev/edge/mediapipe/solutions/vision/hand_landmarker#models) and place it in the project folder. Rename it to `Task.task` or update the `MODEL_PATH` in `hand-tracking.py`.

## Usage

```bash
python hand-tracking.py
```

- Hold your hand in front of the webcam
- Pinch your thumb and index finger together → low volume
- Spread them apart → high volume
- Press `q` to quit

## Hand Landmarks

MediaPipe detects 21 landmarks per hand:

| Index | Landmark |
|-------|----------|
| 0 | Wrist |
| 1-4 | Thumb |
| 5-8 | Index finger |
| 9-12 | Middle finger |
| 13-16 | Ring finger |
| 17-20 | Pinky |

## Requirements

- Python 3.9+
- Webcam
- macOS (for volume control integration)
