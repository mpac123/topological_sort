from os import path

from setuptools import setup, find_packages


def load_requirements():
    try:
        with open("requirements.txt", "r") as f:
            return f.readlines()
    except:
        print("Exception getting requirements.txt file, returning []")
    return []

setup(
    name="topological_sort",
    version="0.1.0",
    description="Project for algorithm analysis course (AAL) in WUT",
    author="Marta Pacuszka",
    install_requires=load_requirements(),
    packages=find_packages(exclude=("tests*", "*tests", "tests")),
    include_package_data=True,
    entry_points='''
        [console_scripts]
        topological_sort=topological_sort.__main__:main
    '''
)