from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()


setup(
    name="AIOFastTelethonHelper",
    version="1.0.0",
    description="Library for fully asynchronous and parallel file upload/download in Telethon, without blocking the event loop",
    packages=find_packages(),
    install_requires=["telethon", "telethon-tgcrypto"],
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Operating System :: OS Independent",
    ],
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Aron1cX/AIOFastTelethonHelper",
    author="Aron1cX",
    author_email="aron1cx.dev@gmail.com"
)
