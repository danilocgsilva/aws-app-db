from setuptools import setup

VERSION = "0.0.1"

def readme():
    with open("README.md") as file:
        return file.read()

setup(
    name="aws-app-db",
    description="Deploys and manages applications with its own database with AWS cloud services",
    long_description_content_type="text/markdown",
    long_description=readme(),
    keywords="AWS deploy manage ec2 virtual machine cloud web application",
    url="git@github.com:danilocgsilva/aws-app-db.git",
    author="Danilo Silva",
    author_email="contact@danilocgsilva.me",
    packages=["src"],
    entry_points={"console_scripts": ["awsweb=src.__main__:main"],},
    include_package_data=True
)
