#This is the program to run motion detecting turret (Prototype Run and will be tweaked later)

#Multiple Steps are required to run this code with Raspberry Pi
# 1. Update all Raspberry Pi System Packages
# 2. Install Python and Pip
# 3. Install Dependencies (OpenCV, AprilTags, RPi.GPIO)
# 4. Connect all Hardware and Setup GPIO Pins


import cv2
import apriltag
import RPi.GPIO as GPIO
import time

# Initialize the webcam
cap = cv2.VideoCapture(0)

# Initialize GPIO pins for stepper motor control
STEP_PIN_X = 11  # Pick PIN number Later
DIR_PIN_X = 12   # Pick PIN number Later

STEP_PIN_Y = 13  # Pick PIN number Later
DIR_PIN_Y = 15   # Pick PIN number Later

# Configure GPIO pins
GPIO.setmode(GPIO.BOARD)
GPIO.setup(STEP_PIN_X, GPIO.OUT)
GPIO.setup(DIR_PIN_X, GPIO.OUT)
GPIO.setup(STEP_PIN_Y, GPIO.OUT)
GPIO.setup(DIR_PIN_Y, GPIO.OUT)

# Create an AprilTag detector
detector = apriltag.Detector()

# Define stepper motor parameters
steps_per_revolution = 200  # Number of steps per revolution of the stepper motor
delay = 0.01  # Delay between steps (adjust for desired speed)

def move_stepper_motor(step_pin, dir_pin, steps):
    GPIO.output(dir_pin, GPIO.HIGH if steps > 0 else GPIO.LOW)
    steps = abs(steps)
    for _ in range(steps):
        GPIO.output(step_pin, GPIO.HIGH)
        time.sleep(delay)
        GPIO.output(step_pin, GPIO.LOW)
        time.sleep(delay)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect AprilTags in the frame
    detections = detector.detect(gray)

    # If AprilTags are detected, control the stepper motors based on their positions
    if detections:
        for detection in detections:
            # Get the center of the tag
            center_x = int(detection.center[0])
            center_y = int(detection.center[1])

            # Calculate steps to move stepper motors
            steps_x = center_x - 320  # Assuming the frame width is 640
            steps_y = center_y - 240  # Assuming the frame height is 480

            # Move stepper motors
            move_stepper_motor(STEP_PIN_X, DIR_PIN_X, steps_x)
            move_stepper_motor(STEP_PIN_Y, DIR_PIN_Y, steps_y)

    # Display the frame
    cv2.imshow('Frame', frame)

    # Break the loop when 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam, cleanup GPIO, and close all OpenCV windows
cap.release()
GPIO.cleanup()
cv2.destroyAllWindows()
