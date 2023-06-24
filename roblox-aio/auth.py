import aiohttp

async def get_csrf_token(self, cookie: str):
	"""Used for getting the x-csrf-token by using the logout endpoint."""
	cookies = {
		'.ROBLOSECURITY': cookie
	}
	async with aiohttp.ClientSession() as session:
		async with session.post(f"https://auth.roblox.com/v2/logout", cookies=cookies) as r:
			return r.headers['x-csrf-token']

class authentication:
    def __init__(self, cookie):
        self.cookie = cookie
        
    async def get_auth(self):
        cookies = {
		'.ROBLOSECURITY': self.cookie 
	}
	headers = {"x-csrf-token": await get_csrf_token(cookie=self.cookie)}
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://users.roblox.com/v1/users/authenticated", cookies=cookies, headers=headers) as response:
                return await response.json()
