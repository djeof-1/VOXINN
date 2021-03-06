import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "voxinn",
    version = "0.0.1",
    author = "Shreyas Iyer",
    author_email = "shreyasiyer14@gmail.com",
    description = ("Voxinn is a Voxel based 3D engine, built in OpenGL."),
    license = "MIT",
    keywords = "3dgameengine engine opengl",
    url = "http://packages.python.org/",
    packages=['voxinn', 'voxinn/heightmap', 'voxinn/terrain', 'voxinn/procedural'],
    long_description=read('README.md'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Topic :: Utilities",
        "License :: OSI Approved :: MIT License",
    ],
)
