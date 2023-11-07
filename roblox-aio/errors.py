class InvalidDisplay(Exception):
	def __init__(self, message):
		self.message = message
		super().__init__(self.message)

class CookieError(Exception):
	def __init__(self, error):
		self.error = error
		super().__init__(self.error)

class AuthenticationError(Exception):
	def __init__(self, error):
		self.error = error
		super().__init__(self.error)
