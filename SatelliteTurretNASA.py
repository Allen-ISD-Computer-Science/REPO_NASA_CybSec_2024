import cv2
import pygame, sys
import pygame.camera
from pygame.locals import *
import os

os.environ['XDG_RUNTIME_DIR'] = '/run/user/1000'

pygame.init()
pygame.camera.init()

screen = pygame.display.set_mode((640, 480))

cam = pygame.camera.Camera("/dev/video0", (640, 480))
cam.start()

while 1:
	image = cam.get_image()
	screen.blit(image,(0, 0))
	pygame.display.update()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
