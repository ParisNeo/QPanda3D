from pathlib import Path
from typing import Union

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


def read_requirements(path: Union[str, Path]):
    with open(path, "r") as file:
        return file.read().splitlines()


requirements = read_requirements("requirements.txt")
requirements_dev = read_requirements("requirements_dev.txt")

setuptools.setup(
    name="QPanda3D",
    version="0.2.10",
    author="Saifeddine ALOUI",
    author_email="aloui.saifeddine@gmail.com",
    description="A binding to use Panda3D as a PySide6 widget",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ParisNeo/QPanda3D",
    packages=setuptools.find_packages(),
    install_requires=requirements,
    extras_require={"dev": requirements_dev},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
)
