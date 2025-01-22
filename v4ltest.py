import cv2

class CameraViewer:
    def __init__(self, dev_video_path):
        self.dev_video_path = dev_video_path
        self.cap = cv2.VideoCapture(self.dev_video_path, cv2.CAP_V4L2)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
        # set fps
        self.cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)
        self.cap.set(cv2.CAP_PROP_FPS, 60)


    def display_video(self):
        if not self.cap.isOpened():
            print("Error: Could not open video device.")
            return

        while True:
            ret = self.cap.grab()
            assert ret
            
            ret, frame = self.cap.retrieve()
            if not ret:
                print("Error: Failed to read frame from video device.")
                break

            # Display the frame
            cv2.imshow("Camera Feed", frame)

            # Break the loop on 'q' key press
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        # Release the video capture object and close windows
        self.cap.release()
        cv2.destroyAllWindows()

if __name__ == "__main__":
    # Replace '/dev/video0' with your video device path if different
    viewer = CameraViewer('/dev/v4l/by-id/usb-USB3.0_4K_Capture_Device_USB3.0_4K_Capture_Device_00000001-video-index0')
    viewer.display_video()
