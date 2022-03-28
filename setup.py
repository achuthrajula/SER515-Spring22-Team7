from setuptools import setup, find_packages

# Specifies the name of the package and the version number
# Is necessary for the package to be recognized by the Python interpreter
# Also helps install the package locally or on the PyPi server

setup(
    name='ezRos',
    version='1.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'ezRos=ezRos.__main__:main',
        ]
    }
)   