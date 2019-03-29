# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(name="kronprod",
      version="1.0",
      author="Justin Wasserman, Alexandra Nilles",
      url="https://github.com/Jbwasse2/Kronecker-Product-Library",
      description="Kronecker Product Library",
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
      py_modules=['kronprod', 'KronMDP'],
      packages=find_packages(),
      install_requires=["numpy", "scipy"])
