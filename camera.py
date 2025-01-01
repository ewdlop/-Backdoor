import cv2

def main():
    # Initialize the webcam (default is 0, change if you have multiple cameras)
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Cannot access the camera.")
        return

    print("Press 'C' to capture an image or 'Q' to quit.")

    while True:
        # Read the video feed
        ret, frame = cap.read()
        if not ret:
            print("Error: Unable to capture video.")
            break

        # Display the video feed
        cv2.imshow("Camera Feed", frame)

        # Keyboard input handling
        key = cv2.waitKey(1) & 0xFF
        if key == ord('c'):
            # Save the current frame
            filename = "captured_image.png"
            cv2.imwrite(filename, frame)
            print(f"Image captured and saved as {filename}")
        elif key == ord('q'):
            # Quit the application
            print("Exiting the application.")
            break

    # Release the camera and close all windows
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
