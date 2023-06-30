from setuptools import setup

setup(
    name="bhc_aws",
    version="0.0.1",
    description="A Python module for working with AWS objects",
    author="Matthew Doiron",
    packages=["bhc_aws"],
    install_requires=['boto3'],
)
