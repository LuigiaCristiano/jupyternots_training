# import sys

# from setuptools import setup, find_packages
from setuptools import setup

version = '0.1'

setup(
    name='jupynote1',
    version=version,
    author='Luigia Cristiano',
    author_email='luigia.cristiano@helmholtz-berlin.de',
    python_requires='!=3.0.*, !=3.1.*, !=3.2.*, <4',
    install_requires=[],
    %packages=[''],
    %package_dir={'': 'src'},
    %entry_points={
     %   'console_scripts': [
      %      ' = :main',
       % ]
    %}
)
