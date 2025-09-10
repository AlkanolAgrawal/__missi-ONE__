from setuptools import setup, find_packages
from src.utils import get_requireds

setup(
    name='movie-recommender',
    version='0.0.1',
    author='Alkanol',
    author_email='coding.alkanol@gmail.com',
    description='A machine learning-powered movie recommendation system',
    packages=find_packages(),
    install_requires=get_requireds('requirements.txt'),
)