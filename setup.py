import os

from setuptools import setup, find_packages


def read(filename):
    with open(os.path.join(os.path.dirname(__file__), filename)) as file:
        return file.read()


setup(
    name='evoker',
    version='0.1.0',
    keywords=['evoker', ],
    url='',
    author='',
    author_email='',
    description='',
    long_description=read('README.md'),
    long_description_content_type="text/markdown",
    packages=find_packages(),
    install_requires=[
        'aiohttp==3.8.1',
        'celery==5.2.3',
        'flower==1.0.0',
        'requests==2.27.1',
    ],
    scripts=[
        'evoker/evoker-cli',
    ]
)
