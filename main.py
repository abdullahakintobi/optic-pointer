# Import necessary libraries
import cv2
import mediapipe as mp
import pyautogui

cam = cv2.VideoCapture(0)
face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
screen_w, screen_h = pyautogui.size()

# Increase sensitivity multiplier to allow small face movements to map more broadly
SENSITIVITY_X = 4.5  # Tune this value
SENSITIVITY_Y = 4.0  # Tune this value

while True:
    _, frame = cam.read()
    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = face_mesh.process(rgb_frame)
    landmark_points = output.multi_face_landmarks
    frame_h, frame_w, _ = frame.shape

    if landmark_points:
        landmarks = landmark_points[0].landmark

        # Using landmark 475 (one of the iris points)
        eye_landmark = landmarks[475]
        x = int(eye_landmark.x * frame_w)
        y = int(eye_landmark.y * frame_h)
        cv2.circle(frame, (x, y), 3, (0, 255, 0))

        # Normalize the coordinates relative to frame center
        dx = (eye_landmark.x - 0.5) * SENSITIVITY_X
        dy = (eye_landmark.y - 0.5) * SENSITIVITY_Y

        # Calculate screen position
        screen_x = screen_w * (0.5 + dx)
        screen_y = screen_h * (0.5 + dy)

        # Ensure the mouse stays within screen bounds
        screen_x = max(0, min(screen_x, screen_w - 1))
        screen_y = max(0, min(screen_y, screen_h - 1))

        pyautogui.moveTo(screen_x, screen_y, duration=0.05)

        # Blink detection for left eye
        left = [landmarks[145], landmarks[159]]
        for landmark in left:
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            cv2.circle(frame, (x, y), 3, (0, 255, 255))

        if (left[0].y - left[1].y) < 0.004:
            pyautogui.click()
            pyautogui.sleep(1)

    cv2.imshow("Eye controlled mouse", frame)
    cv2.waitKey(1)
