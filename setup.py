"""
Setuptools based setup module
"""
from setuptools import setup, find_packages
import versioneer


setup(
    name='pymov2gif',
    version=versioneer.get_version(),
    description='Similar to the Google authenticator just written in python.',
    url='https://github.com/pyscioffice/pymov2gif',
    author='Jan Janssen',
    author_email='jan.janssen@outlook.com',
    license='BSD',
    packages=find_packages(exclude=["*tests*"]),
    install_requires=[],
    cmdclass=versioneer.get_cmdclass(),
    entry_points={
        "console_scripts": [
            'pymov2gif=pymov2gif.__main__:command_line_parser'
        ]
    }
)