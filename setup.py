# -*- coding: utf-8 -*-

from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize
import eigency

extensions = [
    Extension("pysophus.sophus",
        sources=["pysophus/sophus.pyx"],
        include_dirs = [".", "/usr/include/eigen3", "./Sophus"] + eigency.get_includes(include_eigen=False),
        language="c++",
        extra_compile_args=["-std=c++11"]),
]

setup(
    name='pysophus',
    packages=['pysophus'],
    package_dir={'pysophus':'pysophus'},
    version='0.1',
    description='Python bindings for Sophus',
    author='Arnaud Tanguy',
    url='https://github.com/arntanguy',
    ext_modules = cythonize(extensions),
)
