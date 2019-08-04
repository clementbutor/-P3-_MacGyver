import os

import pygame
from bag import Bag
from maze import Maze
from direction import Direction
from gui import GUI


class Game():
	""" This class manages user interactions, victory conditions,
	screen refresh and the main loop.

	"""
	def __init__(self):
		pygame.init()
		# Control how held keys are repeated
		pygame.key.set_repeat(100, 100)
		resolution = (799, 705)
		# The window can be resized
		self.window = pygame.display.set_mode(resolution, pygame.RESIZABLE)
		# Window title
		pygame.display.set_caption("MacGyver")
		self.images = {
			"floor_image": pygame.image.load("media/floor.png").convert_alpha(),
			"wall_image": pygame.image.load("media/wall.png").convert_alpha(),
			"tube_image": pygame.image.load("media/tube.png").convert_alpha(),
			"seringue_image": pygame.image.load("media/seringue.png").convert_alpha(),
			"needle_image": pygame.image.load("media/needle.png").convert_alpha(),
			"guardian_image": pygame.image.load("media/guardian.png").convert_alpha(),
			"ether_image": pygame.image.load("media/ether.png").convert_alpha(),
			"mac_image": pygame.image.load("media/mac.png").convert_alpha()
		}
		self.font = pygame.font.SysFont("herculanum", 35)
		self.bag = Bag()
		self.restart()
		self.run()

	def restart(self):
		# State variable that announces the game mode
		self.state = "running"
		self.bag = Bag()
		self.maze = Maze(self.images, self.bag, self)
		self.gui = GUI(self.font, self.bag, self)

	def face_guardian(self):
		"""Victory if all components have been picked up."""
		self.state = "win" if self.bag.is_full() else "lose"

	def run(self):
		while True:
			for event in pygame.event.get():
				self.on_event(event)
			self.draw()

	def on_event(self, event):
		"""Keyboard events that close the program and move the character."""
		if event.type == pygame.QUIT:
			return pygame.quit()
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				return pygame.quit()

		if event.type == pygame.KEYDOWN:
			if self.state == "running":
				if event.key == pygame.K_UP:
					self.maze.move_macgyver(Direction.Top)
				elif event.key == pygame.K_DOWN:
					self.maze.move_macgyver(Direction.Bottom)
				elif event.key == pygame.K_LEFT:
					self.maze.move_macgyver(Direction.Left)
				elif event.key == pygame.K_RIGHT:
					self.maze.move_macgyver(Direction.Right)
			else:
				self.restart()

	def draw(self):
		""" Draw the window and update the full display Surface to the screen."""
		self.maze.draw(self.window)
		self.gui.draw(self.window)
		# Screen refresh
		pygame.display.flip()
