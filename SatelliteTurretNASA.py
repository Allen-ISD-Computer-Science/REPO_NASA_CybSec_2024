import cv2
import pygame
import numpy as np
import os

os.environ['XDG_RUNTIME_DIR'] = '/run/user/1000'

camera = cv2.VideoCapture(0)

pygame.init()
pygame.display.set_caption("Video Stream")


while True:
	ret, frame = camera.read()
	if not ret:
		break
		
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	gray = cv2.GaussianBlur(gray, (21, 21), 0)
	
	if 'frameDelta' not in locals():
		frameDelta = None
		firstFrame = gray
		
		frameDelta = cv2.absdiff(firstFrame, gray)
		thresh = cv2.threshold(frameDelta, 25, 255, cv2.THRESH_BINARY)[1]
		
		thresh = cv2.dilate(thresh, None, iterations=2)
		contours, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
		
		for contour in contours:
			if cv2.contourArea(contour) < 500:
				continue
			(x, y, w, h) = cv2.boundingRect(contour)
			cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
		
		frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
		surface = pygame.surfarray.make_surface(frame_rgb)
		screen = pygame.display.set_mode((frame.shape[1], frame.shape[0]))
		screen.blit(surface, (0, 0))
		pygame.display.flip()
		
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				break

camera.release
pygame.quit()
