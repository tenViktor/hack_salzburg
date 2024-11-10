import cv2
import os

def detect_persons(video_source=r"C:\Users\brano\Videos\zjazd.mp4"):
    # Initialize counter
    person_count = 0

    # path to the clasifier
    xml_path = r"C:\Users\brano\Desktop\ReactJS\quest22\src\haarcascade_fullbody.xml"
    
    # Load person detection classifier (Haar Cascade)
    classifier = cv2.CascadeClassifier(xml_path)
    
    # Initialize video capture
    cap = cv2.VideoCapture(video_source)
    while True:
        # read a frame from the video source
        ret, frame = cap.read()

        # convert  to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # detect persons
        persons = classifier.detectMultiScale(
            gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30)
        )

        # highlight persons
        for (x, y, w, h) in persons:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # update person count
        person_count = len(persons)

        # display current person count on frame
        cv2.putText(frame, f"Persons: {person_count}", (10, 30), 
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        # show the frame
        cv2.imshow("Person Counter", frame)

        # exit the loop if 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # video capture and close OpenCV windows
    cap.release()
    cv2.destroyAllWindows()

    # return the final count of persons detected
    return person_count

# Example usage
if __name__ == "__main__":
    count = detect_persons()
    if count is not None:
        print(f"Total number of persons detected: {count}")
