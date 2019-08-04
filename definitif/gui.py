
class GUI:
	""" Class that supports text display and states."""

	def __init__(self, font, bag, game):
		self.font = font
		self.bag = bag
		self.game = game

	def draw(self, window):
		text_bag = self.font.render("bag", True, (255, 255, 255))
		text_content = self.font.render(f"{len(self.bag.content)}/3", True, (255, 255, 255))
		text_win = self.font.render("YOU WIN ! press a key to restart", True, (255, 255, 255))
		text_lose = self.font.render("YOU LOSE! press a key to restart", True, (255, 255, 255))
		window.blit(text_bag, (730, 47))
		window.blit(text_content, (738, 70))
		if not self.game.state == "running":
			window.blit(text_win if self.game.state == "win" else text_lose, (
				window.get_width()//2 - text_win.get_width()//2,
				window.get_height()//2 - text_win.get_height()//2
			))
