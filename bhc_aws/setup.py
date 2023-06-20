from setuptools import setup

setup(
    name="bhc_aws",
    version="1.0.0",
    description="A Python module for working with AWS objects",
    author="Matthew Doiron",
    packages=["bhc_secrets"],
    install_requires=['boto3'],
)
