from setuptools import setup, find_packages

VERSION = "0.1.0"
DESCRIPTION = (
    "A package meant to help faciliate the setup.py aspect of Python package distribution."
)

def get_read_me():
    with open("README.md", "r") as f:
        return f.read()

# Setting up
setup(
    name="packagesetup",
    version=VERSION,
    author="Prerit Das",
    author_email="<preritdas@gmail.com>",
    description=DESCRIPTION,
    long_description=get_read_me(),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires = ["wheel", "setuptools"],
    keywords=["python", "tools", "setup", "distribution"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows"
    ],
)