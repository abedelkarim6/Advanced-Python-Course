import cv2

# take a snapshot from the default camera and save it as "snapshot.jpg"
cap = cv2.VideoCapture(0)  # 0 = default camera
ret, frame = cap.read()
cv2.imwrite("snapshot.jpg", frame)
cap.release()


# open the default camera and display the video feed in a window
cap = cv2.VideoCapture(0)  # 0 = default camera
while True:
    ret, frame = cap.read()
    cv2.imshow("Camera Feed", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):  # press 'q' to quit
        break
cap.release()
cv2.destroyAllWindows()
