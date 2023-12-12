from setuptools import setup, find_packages

setup(
    name='nazara',
    version='0.0.1',
    description='We are legion',
    author='Spencer Everett',
    author_email='spencerweverett@gmail.com',
    url='https://github.com/sweverett/nazara',
    packages=find_packages(),
    install_requires=['numpy', 'astropy', 'pyyaml', 'galsim'],
)