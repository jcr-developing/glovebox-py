from setuptools import find_packages, setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name='console_gb',
    package_dir={"": "app"},
    packages=find_packages(where="app"),
    version='0.1.0',
    description='Library that will help with common console interactions',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jcr-developing/glovebox-py",
    author='jcr-developing',
    author_email="josuesalvador5@hotmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.12",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
        "Topic :: Terminals",
        ],
    install_requires=[],
    extras_requires={
        "dev": ['pytest>=8.3.3', 'pytest-runner>=6.0.1', 'twine>=5.1.1'],
    },
)