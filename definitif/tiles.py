
class Tile:

	def __init__(self, image):
		self.image = image

	def draw(self, window, x, y):
		window.blit(self.image, (x, y))


class Floor(Tile):
	def __init__(self, image):
		super().__init__(image)


class Wall(Tile):
	def __init__(self, image):
		super().__init__(image)




class Guardian(Tile):
	def __init__(self, image):
		super().__init__(image)


class McGyver(Tile):
	def __init__(self, image):
		super().__init__(image)

	def collect(self):
		pass		