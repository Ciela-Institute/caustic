from setuptools import setup, find_packages
import os

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name="caustic",
    version="1.0.0",    
    description="Sorry we renamed to: caustics. Please run: pip install caustics",
    long_description=read("README.md"),
    long_description_content_type='text/markdown',
    url="https://github.com/Ciela-Institute/caustic",
    author="Ciela Institute",
    license="MIT license",
    packages=find_packages(),
    install_requires=["numpy"],
    classifiers=[
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",  
        "Programming Language :: Python :: 3",
    ],
)
