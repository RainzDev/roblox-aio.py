import aiohttp
import inspect
from .auth import authentication
from .errors import InvalidDisplay, CookieError, AuthenticationError

class User:
	def __init__(self, cookie: str=None):
		self.cookie = cookie
		
		
	async def change_display_name(self, name: str):
		frame = inspect.currentframe()
		if not self.cookie:
			raise CookieError(f"Cookie is required for function '{inspect.getframeinfo(frame).function}'")
		data = {"newDisplayName": name}
		auth = authentication(cookie=self.cookie)
		_id = await auth.get_auth()
		_id = _id['id']
		cookies = {'.ROBLOSECURITY': self.cookie}
		headers = {"x-csrf-token": await auth.get_csrf_token()}
		async with aiohttp.ClientSession() as session:
			async with session.patch(f"https://users.roblox.com/v1/users/{_id}/display-names", json=data, headers=headers, cookies=cookies) as response:
				r = await response.json()
				if "errors" in r:
					if r["errors"][0]["code"] == 4:
						raise InvalidDisplay(f"String '{name}' cannot be displayed as it has been moderated")
					elif r["errors"][0]["code"] == 3:
						raise InvalidDisplay(f"String '{name}' contains invalid characters")
					elif r["errors"][0]["code"] == 2:
						raise InvalidDisplay(f"String size '{name}' is too long")
					elif r["errors"][0]["code"] == 1:
						raise InvalidDisplay(f"String size '{name}' is too short")
					elif r["errors"][0]["code"] == 0:
						raise AuthenticationError("Cookie is invalid or no cookie was set")
				else:
					return r
