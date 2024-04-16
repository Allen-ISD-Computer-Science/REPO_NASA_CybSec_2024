import cv2
import pygame, sys
import pygame.camera
from pygame.locals import *
import os
import numpy as np
from adafruit_motorkit import MotorKit
import time
import math

os.environ['XDG_RUNTIME_DIR'] = '/run/user/1000'

#initialize everything
pygame.init()
pygame.camera.init()

kit = MotorKit()




#set screen
screen = pygame.display.set_mode((320, 240))

cam = pygame.camera.Camera("/dev/video0", (320, 240)) #set camera in use
cam.start()

fgbg = cv2.createBackgroundSubtractorMOG2()




#Set all constants
X_STEPS_PER_PIXEL = 0.4

Y_STEPS_PER_PIXEL = 0.4

FRAME_RATE = 60

STEP_DELAY = 1 / (0.5 * FRAME_RATE)

MAX_ANGLE_THRESHOLD = 60

FIXED_WIDTH = 100
FIXED_HEIGHT = 100

X_REF_STEPS = 0
Y_REF_STEPS = 0



#Calibrate the motors

def move_to_reference_position():
	kit.stepper1.onestep(direction = 0)
	kit.stepper2.onestep(direction = 0)
	time.sleep(0.1)
print("Moving to Reference Point")
move_to_reference_position()
print("Finished moving to Reference Point")



#Create infinite loop until closed
while 1:
	
	start_time = time.time() #defines start time
	
	image = cam.get_image() #grabs frame from camera
	
	#define contour shape that motion tracker will track
	frame = pygame.surfarray.array3d(image)
	frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
	fgmask = fgbg.apply(frame)
	contours, _ = cv2.findContours(fgmask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
	max_contour = max(contours, key=cv2.contourArea)

	if max_contour is not None:
		
		#Created shape of contour and defines it with its color
		x, y, w, h = cv2.boundingRect(max_contour)
		center_x = x + w // 2
		center_y = y + h // 2
		x1 = center_x - FIXED_WIDTH // 2
		y1 = center_y - FIXED_HEIGHT // 2
		x2 = x1 + FIXED_WIDTH
		y2 = y1 + FIXED_HEIGHT
		cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
		
		
		#now create target movement for motor and max and minimum distances it can move
		target_x = frame.shape[1] // 2
		target_y = frame.shape[0] // 2
		error_x = target_x - (x + w // 2)
		error_y = target_y - (y + h // 2)
		
		x_steps = int(error_x * X_STEPS_PER_PIXEL)
		y_steps = int(error_y * Y_STEPS_PER_PIXEL)
		max_x_steps = int(math.tan(math.radians(MAX_ANGLE_THRESHOLD)) * (h // 2) * X_STEPS_PER_PIXEL)
		max_y_steps = int(math.tan(math.radians(MAX_ANGLE_THRESHOLD)) * (w // 2) * Y_STEPS_PER_PIXEL)
		
		x_steps = min(max_x_steps, max(x_steps, -max_x_steps))
		y_steps = min(max_y_steps, max(y_steps, -max_y_steps))
		
		
		#Program to move motor
		if x_steps > 0:
			for _ in range(x_steps):
				kit.stepper1.onestep(direction=1)
				print("Moved to Right")
				time.sleep(STEP_DELAY)
		elif x_steps < 0:
			for _ in range(abs(x_steps)):
				kit.stepper1.onestep(direction=0)
				print("Moved to Left")
				time.sleep(STEP_DELAY)
		if y_steps > 0:
			for _ in range(y_steps):
				kit.stepper2.onestep(direction=1)
				print("Moved Up")
				time.sleep(STEP_DELAY)
		elif y_steps < 0:
			for _ in range(abs(y_steps)):
				kit.stepper2.onestep(direction=0)
				print("Moved Down")
				time.sleep(STEP_DELAY)
				
		elapsed_time = time.time() - start_time #defines the amount of time that has passed
	
	#ending frame color conversions to allow live video to show on PyGame		
	frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
	image = pygame.surfarray.make_surface(frame)
	screen.blit(image,(0, 0))
	pygame.display.update()
	
	elapsed_time = time.time() - start_time
	
	time.sleep(max(0, STEP_DELAY - elapsed_time))
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
