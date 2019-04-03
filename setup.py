# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(name="kronprod",
      version="1.1",
      author="Justin Wasserman, Alexandra Nilles",
      author_email="jbwasse2@illinois.edu",
      url="https://github.com/Jbwasse2/kronprod",
      description="Kronecker Product Library",
      python_requires='>3.3',
      long_description=" ",
      classifiers=[
          "Programming Language :: Python",
          "Programming Language :: Python :: 3.4",
          "Programming Language :: Python :: 3.5",
          "Programming Language :: Python :: 3.6",
          "Programming Language :: Python :: 3.7",
          "Topic :: Scientific/Engineering",
          "Topic :: Scientific/Engineering :: Mathematics",
          "Topic :: Software Development :: Libraries :: Python Modules"],
      platforms=["Any"],
      license="MIT",
#      packages=find_packages(exclude=['test']),
    #  package_dir={"": "src"},
    #  py_modules=['kronprod', 'KronMDP'],
      packages=['kronprod'],
      package_dir={'kronprod': './src'},
      install_requires=["numpy", "scipy"])
