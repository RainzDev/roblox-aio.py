import aiohttp

class authentication:
	def __init__(self, cookie):
		self.cookie = cookie

	async def get_csrf_token(self):
		"""Used for getting the x-csrf-token by using the logout endpoint."""
		cookies = {
			'.ROBLOSECURITY': self.cookie
		}
		async with aiohttp.ClientSession() as session:
			async with session.post(f"https://auth.roblox.com/v2/logout", cookies=cookies) as r:
				return r.headers['x-csrf-token']
		
	async def get_auth(self):
		cookies = {
		'.ROBLOSECURITY': self.cookie 
		}
		headers = {"x-csrf-token": await self.get_csrf_token()}
		async with aiohttp.ClientSession() as session:
			async with session.get(f"https://users.roblox.com/v1/users/authenticated", cookies=cookies, headers=headers) as response:
				return await response.json()
