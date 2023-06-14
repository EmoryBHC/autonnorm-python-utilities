from setuptools import setup

setup(
    name="bhc_secrets",
    version="1.0.0",
    description="A Python module for autonorm",
    author="Your Name",
    packages=["bhc_secrets"],
    install_requires=[
        'git+https://github.com/EmoryBHC/autonorm-python-utilities.git@main#subdirectory=bhc_utilities'
    ],
)
