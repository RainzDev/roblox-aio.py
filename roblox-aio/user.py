import aiohttp
import endpoints
from .auth import authentication, get_csrf_token

class User:
    def __init__(self, cookie):
        self.cookie = cookie
        
        
    async def change_display_name(self, name: str):
        data = {"newDisplayName": name}
        _id = await authentication()
        headers = {}
        async with aiohttp.ClientSession() as session:
            async with session.patch(f"{endpoints.users}/users/{_id}/display-names") as response:
                r = await response.json()
                if "errors" in r["data"]:
                    pass
                else:
                    return True
