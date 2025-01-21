from setuptools import setup, find_packages

# Helper function to read requirements.txt
def read_requirements():
    with open("requirements.txt") as f:
        return f.read().splitlines()

setup(
    name="simple_project",
    version="0.1",
    packages=find_packages(),
    install_requires=read_requirements(),
    tests_require=["pytest"],
    entry_points={
        "console_scripts": [
            "greet=src.main:greet",
        ],
    },
)