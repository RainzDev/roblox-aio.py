# roblox-aio.py
A Python package that uses aiohttp to request Roblox data.

# Quick Example
Here's an example where you can change the account's display name
```
from roblox-aio import User

user = User(cookie="cookie")
await user.change_display_name(name="any_name")
```
