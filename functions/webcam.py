import cv2
import streamlit as st
from functions.helper import  display_tracker_options, display_detected_frames
from functions import settings
import time

# Webcam function
def play_webcam(conf, model):
    """
    Plays a webcam stream. Detects Objects in real-time using the YOLOv8 object detection model.

    Parameters:
        conf: Confidence of YOLOv8 model.
        model: An instance of the `YOLOv8` class containing the YOLOv8 model.

    Returns:
        None
    """
    # Use webcam source (0 for the default webcam)
    source_webcam = 0  # You can adjust this if using external webcam or specific path
    
    if st.sidebar.button('Detect Objects'):
        try:
            # Open the webcam video stream
            vid_cap = cv2.VideoCapture(source_webcam)
            if not vid_cap.isOpened():
                st.sidebar.error("Error: Unable to open webcam.")
                return

            st_frame = st.empty()  # Placeholder for the stream

            while vid_cap.isOpened():
                success, image = vid_cap.read()
                if success:
                    # Optional: Resize the frame for better display in Streamlit
                    image = cv2.resize(image, (640, 480))

                    # Perform detection and display the frame
                    display_detected_frames(conf, model, st_frame, image)

                    # Show the frame in Streamlit
                    st_frame.image(image, channels="BGR", use_column_width=True)

                    # Small delay to simulate frame rate
                    time.sleep(0.03)  # 30ms delay (~30fps)
                else:
                    st.sidebar.error("Failed to capture video.")
                    break
            vid_cap.release()
        except Exception as e:
            st.sidebar.error(f"Error loading video: {str(e)}")
