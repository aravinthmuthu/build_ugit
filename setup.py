from setuptools import setup, find_packages

setup(
    name='ugit',
    version='0.1',
    description='building my own git from scratch',
    author='Aravinth Muthu',
    packages=find_packages(include=['build_ugit']),
    entry_points={
        'console_scripts': ['ugit=ugit.cli:main']
    }

)