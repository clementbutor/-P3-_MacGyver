from component import Component, Needle, Tube, Ether


class Bag:
	""" Class that contains the components in a list."""

	def __init__(self):
		self.content = []

	def is_full(self):
		return len(self.content) == 3

	def add(self, component):
		self.content.append(component)
