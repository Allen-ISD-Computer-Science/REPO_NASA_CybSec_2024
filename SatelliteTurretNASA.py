import cv2
import pygame, sys
import pygame.camera
from pygame.locals import *
import os
import numpy as np

os.environ['XDG_RUNTIME_DIR'] = '/run/user/1000'

pygame.init()
pygame.camera.init()

screen = pygame.display.set_mode((640, 480))

cam = pygame.camera.Camera("/dev/video0", (640, 480))
cam.start()

fgbg = cv2.createBackgroundSubtractorMOG2()

while 1:
	image = cam.get_image()
	
	frame = pygame.surfarray.array3d(image)
	frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
	fgmask = fgbg.apply(frame)
	contours, _ = cv2.findContours(fgmask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
	
	for contour in contours:
		if cv2.contourArea(contour) > 100:
			x,  y, w, h = cv2.boundingRect(contour)
			cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
	
	frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
	image = pygame.surfarray.make_surface(frame)
	screen.blit(image,(0, 0))
	pygame.display.update()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
