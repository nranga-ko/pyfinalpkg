from setuptools import setup, find_packages

setup(
    name='pyfinalpkg',
    version='0.1',
    description='A sample package with multiple modules',
    author='nranga',
    url='git@github.com:nranga-ko/pyfinalpkg.git',
    author_email='nranga@coca-cola.com',
    packages=find_packages(),
    install_require=['pandas','datetime']
)