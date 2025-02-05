from setuptools import setup
import os

with open("LAMDA_TALENT/requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="lamda_talent",
    version="0.1.0",
    description="A machine learning library for tabular data.",
    packages=["lamda_talent"],
    install_requires=requirements,
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Science/Research",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
)