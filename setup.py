from setuptools import setup
from bimon.metadata import Metadata

metadata = Metadata()


def requirements():
    """Build the requirements list for this project"""
    requirements_list = []

    with open('requirements.txt') as requirements:
        for install in requirements:
            requirements_list.append(install.strip())

    return requirements_list

long_description = """
    Fork from pyCoinmon
"""

setup(
    name = 'bimon',
    packages = ['bimon'],
    install_requires = requirements(),
    version = metadata.get_version(),
    license = 'MIT',
    description = 'The Binance cryptocurrency price tool on CLI',
    long_description= long_description,
    author = metadata.get_author(),
    author_email = 'lokiheero@gmail.com',
    url = 'https://github.com/lokiheero/bimon/',
    download_url = 'https://github.com/lokiheero/bimon/archive/v'+metadata.get_version()+'.tar.gz',
    entry_points={
        'console_scripts': ['bimon=bimon.main:main'],
    },
    keywords = 'Binance criptocurrency crypto ticker python cli price-tracker command-line',
    classifiers = ['Programming Language :: Python',
                   'Programming Language :: Python :: 2.7',
                   'Programming Language :: Python :: 3.2',
                   'Programming Language :: Python :: 3.3',
                   'Programming Language :: Python :: 3.4',
                   'Programming Language :: Python :: 3.5',
                   'Programming Language :: Python :: 3.6'],
)