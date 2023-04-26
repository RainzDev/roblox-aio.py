import aiohttp
import endpoints

async def get_csrf_token(self, cookie: str):
	cookies = {
		'.ROBLOSECURITY': cookie
	}
	async with aiohttp.ClientSession() as session:
		async with session.post("https://auth.roblox.com/v2/logout", cookies=cookies) as r:
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
            async with session.get(f"{endpoints.users}/users/authenticated", cookies=cookies, headers=headers) as response:
                return await response.json()
