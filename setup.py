from setuptools import setup, find_packages
from typing import List

HYPHEN_E_DOT = "-e ."

def get_requirements(file_path: str) -> List[str]:
    '''
    Reads a requirements file and returns a clean list of dependencies.
    '''
    requirements = []
    try:
        with open(file_path, "r") as file_obj:
            requirements = file_obj.readlines()
            requirements = [req.strip() for req in requirements if req.strip()]  # Remove empty lines
            if HYPHEN_E_DOT in requirements:
                requirements.remove(HYPHEN_E_DOT)  # Remove '-e .'
    except FileNotFoundError:
        print(f"Warning: {file_path} not found. Proceeding with an empty requirement list.")

    return requirements

setup(
    name="GENERIC-ML",
    version="0.0.1",
    author="Andrew Melendez",
    author_email="melendeza895@outlook.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),  # No '-e .' here
)
