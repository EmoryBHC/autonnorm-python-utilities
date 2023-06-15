from setuptools import setup

setup(
    name="bhc_secrets",
    version="1.0.0",
    description="A Python module for working with AWS SecretsManager (or other future Secrets managers)",
    author="Matthew Doiron",
    packages=["bhc_secrets"],
    install_requires=['boto3'],
)
