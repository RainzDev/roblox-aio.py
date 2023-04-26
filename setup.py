import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup_info = {
    "name": "roblox-aio",
    "version": "1.0.0",
    "author": "RainzDev",
    "description": "roblox-aio.py is a Roblox API wrapper that uses aiohttp to grab the data.",
    "long_description": long_description,
    "long_description_content_type": "text/markdown",
    "url": "https://github.com/RainzDev/roblox-aio.py/",
    "packages": setuptools.find_packages(),
    "classifiers": [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Framework :: AsyncIO",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content :: CGI Tools/Libraries",
        "Topic :: Software Development :: Libraries"
    ],
    "project_urls": {
        "Issue Tracker": "https://github.com/RainzDev/roblox-aio.py/issues",
        "GitHub": "https://github.com/RainzDev/roblox-aio.py/"
    },
    "python_requires": '>=3.7',
    "install_requires": [
        "aiohttp>=3.8.4",
    ]
}


setuptools.setup(**setup_info)
