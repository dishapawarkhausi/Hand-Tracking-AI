import cv2
import mediapipe as mp

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)

# Define finger landmarks
finger_tips = [8, 12, 16, 20]  # Index, Middle, Ring, Pinky
thumb_tip = 4  # Thumb tip index

# Colors for fingertips (BGR format)
finger_colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255)]

# Start video capture
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Apply Mirror Effect (Flip Horizontally)
    frame = cv2.flip(frame, 1)

    # Convert BGR to RGB for processing
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb_frame)

    # Initialize finger counters
    left_hand_fingers = 0
    right_hand_fingers = 0

    if result.multi_hand_landmarks and result.multi_handedness:
        for idx, hand_landmarks in enumerate(result.multi_hand_landmarks):
            # Get hand label (Left or Right)
            label = result.multi_handedness[idx].classification[0].label
            landmarks = hand_landmarks.landmark
            fingers = []

            # Thumb detection (compared to index base)
            if (label == "Right" and landmarks[thumb_tip].x < landmarks[thumb_tip - 1].x) or \
               (label == "Left" and landmarks[thumb_tip].x > landmarks[thumb_tip - 1].x):
                fingers.append(1)  # Thumb is open
            else:
                fingers.append(0)

            # Count fingers (Index, Middle, Ring, Pinky)
            for i, tip in enumerate(finger_tips):
                if landmarks[tip].y < landmarks[tip - 2].y:  # Tip is above PIP joint
                    fingers.append(1)
                else:
                    fingers.append(0)

                # Draw colored fingertip markers
                h, w, _ = frame.shape
                cx, cy = int(landmarks[tip].x * w), int(landmarks[tip].y * h)
                cv2.circle(frame, (cx, cy), 10, finger_colors[i], -1)

            # Count total open fingers
            fingers_count = fingers.count(1)

            # Assign to left or right hand
            if label == "Right":
                right_hand_fingers = fingers_count
            else:
                left_hand_fingers = fingers_count

            # Draw hand landmarks
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

    # Calculate total fingers
    total_fingers = left_hand_fingers + right_hand_fingers

    # Display the finger count
    cv2.putText(frame, f'Left Hand: {left_hand_fingers}', (50, 100),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    cv2.putText(frame, f'Right Hand: {right_hand_fingers}', (50, 150),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
    cv2.putText(frame, f'Total Fingers: {total_fingers}', (50, 200),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # Show the output
    cv2.imshow("Finger Counting", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam
cap.release()
cv2.destroyAllWindows()
