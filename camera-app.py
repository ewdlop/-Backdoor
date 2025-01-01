Creating a camera app in Python is straightforward using libraries like OpenCV. Below is an example code for a basic camera app:

### Features:
1. Opens the camera feed.
2. Displays the video feed in a window.
3. Captures an image when you press the `C` key.
4. Exits the application when you press the `Q` key.

### Code:

```python
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
```

### Steps to Run:
1. Install OpenCV if not already installed:
   ```bash
   pip install opencv-python
   ```
2. Save the code in a file, e.g., `camera_app.py`.
3. Run the script:
   ```bash
   python camera_app.py
   ```
4. Use the live feed:
   - Press **C** to capture and save an image.
   - Press **Q** to exit.

This is a simple yet functional camera application. It can be extended to include features like video recording, filters, or real-time image processing.
