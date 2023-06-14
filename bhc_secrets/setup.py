from setuptools import setup
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name="bhc_secrets",
    version="1.0.0",
    description="A Python module for autonorm",
    author="Your Name",
    packages=["bhc_secrets"],
    install_requires=requirements,

)
