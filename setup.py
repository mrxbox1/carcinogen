from setuptools import setup
from src.carcinogen import carcinogen

setup(
    name='carcinogen',
    version=carcinogen.CURRENT_VERSION,
    description='MD-to-HTML "converter"',
    author='mrxbox1',
    packages=['carcinogen']
)