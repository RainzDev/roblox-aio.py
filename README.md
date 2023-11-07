# roblox-aio.py
A Python package that uses aiohttp to request Roblox data.

# Quick Example
Here's an example where you can change the account's display name
```py
import asyncio
from roblox_aio import user

user = user.User("cookie")

async def change_display():
    await user.change_display_name(name="name")

asyncio.run(change_display())
```
