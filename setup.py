from setuptools import find_packages
from setuptools import setup

long_description = """
This is a sample project. It is the way how I could create a sw with all the
build and test scripts. It includes all the batch files to be called from the
build system, and 3 levels of testing.
The sample sw is doing rot13 encoding/decoding in quite a complicated way for
demonstration purposes. For more info see http://decode.org/ or
https://docs.python.org/3/library/codecs.html?highlight=rot13#text-transforms
"""

setup(
    name="mysw",
    version="1.0",
    url="https://github.com/bigbirdcode/sampleproject",
    license="MIT License",
    author="BigBirdCode",
    author_email="na",
    description="Sample project with build scripts and tests.",
    long_description=long_description,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Desktop Environment",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Topic :: Development",
        "Topic :: Utilities",
    ],
    packages=find_packages("src"),
    package_dir={"": "src"},
    include_package_data=True,
    python_requires=">=3.5",
    install_requires=[],
    extras_require={
        "dev": [
            "pytest",
            "pytest-bdd",
            "flake8",
            "pylint",
        ],
    },
    entry_points={"cli_scripts": ["mysw = mysw.main:main"]},
)
