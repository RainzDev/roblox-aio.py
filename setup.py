from setuptools import setup

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='roblox-aio.py',
    version='1.0.4',
    url="https://github.com/RainzDev/roblox-aio.py",
    description='A Roblox API wrapper used for getting data from Roblox API.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='RainzDev',
    author_email='jessrblx16@gmail.com',
    license='MIT',
    packages=['roblox_aio'],
    install_requires=['numpy', 'aiohttp', 'wheel'],
)
