from setuptools import setup, find_packages

setup(
    name="arriva-gal",
    version="0.3.0",
    author="Alfonso Pérez Sánchez",
    author_email="alfonso.perezsanchez@hotmail.com",
    description="API wrapper for Arriva Galicia",
    packages=find_packages(),
    keywords=['bus', 'public transport', 'galicia', 'api', "arriva"],
    install_requires=[
        "requests",
    ]
)
