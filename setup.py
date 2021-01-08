from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='optus',
    version='0.0.1',
    author="itchannel",
    author_email="steve@itchannel.me",
    description="Python wrapper for the optus mobile API",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/itchannel/optus-api",
    license="MIT",
    packages=['optus'],
    scripts=['optus/bin/demo.py'],
    classifiers=[
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=['requests']
)
