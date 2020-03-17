#setup.py
import setuptools
from setuptools import find_packages, setup

REQUIRED = [
    "numpy"
    "pandas"
    "scikit-learn"
    "matplotlib"
    "catagory-encoders"
]
with open("README.md", "r") as fh:
    long_description = fh.read()
    setuptools.setup(
        name="amin_toolbox",
        version="1.1",
        author="Amin Azad",
        author_email="amindazad@icloud.com",
        description="nice display for null values and train test val spliting",
        long_description=long_description,
        long_description_content_type="text/markdown", # required if using a md file for long desc
        #license="MIT",
        url="https://github.com/amindazad/lambdata-12",
        keywords="",
        packages=find_packages() # ["game_utils"]
    )