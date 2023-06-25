import aiohttp
from .auth import authentication, get_csrf_token

class InvalidDisplay(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class User:
    def __init__(self, cookie):
        self.cookie = cookie
        
        
    async def change_display_name(self, name: str):
        data = {"newDisplayName": name}
        auth = authentication(cookie=self.cookie)
        _id = await auth.get_auth()['id']
        cookies = {
		'.ROBLOSECURITY': self.cookie 
	}
	headers = {"x-csrf-token": await get_csrf_token(cookie=self.cookie)}
        async with aiohttp.ClientSession() as session:
            async with session.patch(f"https://users.roblox.com/v1/users/{_id}/display-names", json=data}) as response:
                r = await response.json()
		if "errors" in r["data"]:
                	if r["data"]["errors"][0]["code"] == 4:
                    		raise InvalidDisplay(f"String '{name}' cannot be displayed as it has been moderated")
			elif r["data"]["errors"][0]["code"] == 3:
                		raise InvalidDisplay(f"String '{name}' contains invalid characters")
			elif r["data"]["errors"][0]["code"] == 2:
                		raise InvalidDisplay(f"String size '{name}' is too long")
			elif r["data"]["errors"][0]["code"] == 1:
                		raise InvalidDisplay(f"String size '{name}' is too short")
		else:
			return r
