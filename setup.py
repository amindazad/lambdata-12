#setup.py

from setuptools import find_packages, setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="lambda_functions",
    version="1.0",
    author="Amin Azad",
    author_email="amindazad@icloud.com",
    description="nice display for null values and train test spliting",
    long_description=long_description,
    long_description_content_type="text/markdown", # required if using a md file for long desc
    #license="MIT",
    url="https://github.com/amindazad/lambdata-12",
    keywords="",
    packages=find_packages() # ["game_utils"]
)