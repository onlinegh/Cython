# -*- coding: utf-8 -*-
"""
Created on Sat May 25 11:27:36 2019

@author: PA389009
"""

from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
ext_modules = [
    Extension("main",  ["main.py"]),
    #all your modules that need be compiled ...
]
setup(
    name = 'My Program Name',
    cmdclass = {'build_ext': build_ext},
    ext_modules = ext_modules
)
