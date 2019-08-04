from random import randint

from component import Component, Needle, Tube, Ether
from tiles import Floor, Wall, McGyver, Guardian
from direction import Direction
from bag import Bag
from gui import GUI


class Maze:
	""" Class to create the maze with its components,
	draw it and move the character inside.

	"""
	def __init__(self, images, bag, game):
		self.images = images
		self.__load()
		self.randomize_components()
		self.bag = bag
		self.game = game

	def __load(self):
		""" Maze creation with Tile instances, using the external file."""
		with open("level.txt") as file:
			data = file.read()
			# Split data into a list, using line break as a separator
			lines = data.split('\n')
			self.tiles = []
			for line in lines:
				line_tiles = []
				for tile in line:
					if tile == " ":
						line_tiles.append(Floor(self.images["floor_image"]))
					elif tile == "#":
						line_tiles.append(Wall(self.images["wall_image"]))
					elif tile == "M":
						line_tiles.append(McGyver(self.images["mac_image"]))
					elif tile == "G":
						line_tiles.append(Guardian(self.images["guardian_image"]))
				self.tiles.append(line_tiles)

	def randomize_components(self):
		""" It randomly distributes the components into empty cells."""
		for comp in (
			Tube(self.images["tube_image"]),
			Needle(self.images["needle_image"]),
			Ether(self.images["ether_image"])
		):
			while True:
				col, row = randint(0, 14), randint(0, 14)
				if isinstance(self.tiles[row][col], Floor):
					self.tiles[row][col] = comp
					break

	def is_wall(self, row, col):
		return type(self.tiles[row][col]) == Wall

	def is_guardian(self, row, col):
		return type(self.tiles[row][col]) == Guardian

	def draw(self, window):
		""" Method for displaying the level."""
		window.fill((0, 0, 0))
		for row, line in enumerate(self.tiles):
			for col, tile in enumerate(line):
				x = col * 47
				y = row * 47
				tile.draw(window, x, y)

	def find_tile(self, cls):
		for row_id, row in enumerate(self.tiles):
			for col_id, tile in enumerate(row):
				if tile.__class__ == cls:
					return col_id, row_id
		return None

	def find_mac(self):
		return self.find_tile(McGyver)

	def is_component(self, row, col):
		return isinstance(self.tiles[row][col], Component)

	def move_macgyver(self, direction):
		""" Method to move the character."""
		col, row = self.find_mac()
		if direction == Direction.Right:
			# Tests the limits
			if col < 14:
				# Tests obstacles
				if not self.is_wall(row, col + 1):
					if self.is_component(row, col + 1):
						# Adds the component to the Content list
						self.bag.add(Component)
					elif self.is_guardian(row, col + 1):
						self.game.face_guardian()
					self.tiles[row][col] = Floor(self.images['floor_image'])
					self.tiles[row][col + 1] = McGyver(self.images['mac_image'])

		elif direction == Direction.Left:
			if col > 0:
				if not self.is_wall(row, col - 1):
					if self.is_component(row, col - 1):
						self.bag.add(Component)
					elif self.is_guardian(row, col - 1):
						self.game.face_guardian()
					self.tiles[row][col] = Floor(self.images['floor_image'])
					self.tiles[row][col - 1] = McGyver(self.images['mac_image'])

		elif direction == Direction.Top:
			if row > 0:
				if not self.is_wall(row - 1, col):
					if self.is_component(row - 1, col):
						self.bag.add(Component)
					elif self.is_guardian(row - 1, col):
						self.game.face_guardian()
					self.tiles[row][col] = Floor(self.images['floor_image'])
					self.tiles[row - 1][col] = McGyver(self.images['mac_image'])

		elif direction == Direction.Bottom:
			if row < 14:
				if not self.is_wall(row + 1, col):
					if self.is_component(row + 1, col):
						self.bag.add(Component)
					elif self.is_guardian(row + 1, col):
						self.game.face_guardian()
					self.tiles[row][col] = Floor(self.images['floor_image'])
					self.tiles[row + 1][col] = McGyver(self.images['mac_image'])
