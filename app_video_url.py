import cv2
import mediapipe as mp
import pafy

url = "https://www.youtube.com/watch?v=Or52aH46crI"
mp_drawing = mp.solutions.drawing_utils
mp_drawing_style = mp.solutions.drawing_styles
mp_drawing_spec = mp_drawing_style.get_default_pose_landmarks_style()
mp_pose = mp.solutions.pose

video = pafy.new(url)
stream = video.getbest("mp4")
cap = cv2.VideoCapture(stream.url)
with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
    while cap.isOpened():
        if 27 == 0xFF & cv2.waitKey(1):
            break

        success, image = cap.read()
        if not success:
            print("empty video frame")
            break

        results = pose.process(image)
        mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
        cv2.imshow("pose detection", image)

cap.release()
cv2.destroyAllWindows()