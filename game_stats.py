

class GameStats():
	"""docstring for GameStats"""
	def __init__(self, ai_settings):
		self.ai_settings = ai_settings
		self.reset_stats()

		#start Alien Invansion in an active state.
		self.game_active = False

		# High score should never be reset.
		self.high_score = 0

	def reset_stats(self):
		"""Initialize statistics that can change during the game."""
		self.ships_left = self.ai_settings.ship_limit
		self.score = 0
		self.level = 1






		
