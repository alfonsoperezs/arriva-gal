from setuptools import setup, find_packages

VERSION = '0.3.0.0'
DESCRIPTION = 'Python API wrapper for the galician public transport'

setup(
    name="arrivagal",
    version="0.1",
    author="Alfonso Pérez Sánchez",
    author_email="alfonso.perezsanchez@hotmail.com",
    description="API wrapper for Arriva Galicia",
    packages=find_packages(),
    keywords=['bus', 'public transport', 'galicia', 'api', "arriva"]
)