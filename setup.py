from setuptools import setup

REQUIREMENTS = [i.strip() for i in open("requirements.txt").readlines()]


setup(
    name="FANTASTIC_FOUR_PROJB",
    version="10.0",
    packages=[""],
    url="",
    license="MIT Commons",
    author="Ryan van Lil-Reddy",
    author_email="ryanreddy@hotmail.com",
    description="SteamAPI based data gamedataviewer",
    install_requires=REQUIREMENTS,
)

print("running installer")
