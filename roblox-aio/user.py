import aiohttp
from .auth import authentication, get_csrf_token
from .errors import InvalidDisplay, CookieError

class User:
	"""Represents the user
 	Attributes:
  		id: Grabs the current user ID
		name: Grabs the current user name
  		display_name: Grabs the current display name"""
    def __init__(self, cookie: str=None):
        self.cookie = cookie
        
        
    async def change_display_name(self, name: str):
		"""Changes the account display name
		
  		"""
		if not self.cookie:
			raise CookieError
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
