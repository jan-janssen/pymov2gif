"""
Setuptools based setup module
"""
from setuptools import setup, find_packages
from pathlib import Path
import versioneer


setup(
    name='pymov2gif',
    version=versioneer.get_version(),
    description='Convert *.mov to *.gif',
    long_description=Path("README.md").read_text(),
    long_description_content_type='text/markdown',
    url='https://github.com/jan-janssen/pymov2gif',
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