from setuptools import setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="tabletopia-discord-bot",
    version="1.0",
    description="A discord bot for picking tabletopia games",
    license="MIT",
    long_description=long_description,
    author="Anthony Panettiere",
    packages=["tabletopia-discord-bot"],  # same as name
)
