from setuptools import Extension, setup
from Cython.Build import cythonize

ext_modules = [
    Extension("csin",
              sources=["libc_sin.pyx"],
              libraries=["m"]
    )
]

setup(name="csin", ext_modules=cythonize(ext_modules))