#!/usr/bin/env python
from setuptools import setup

setup(name="multipool",
      version="0.10.3",
      description="Efficient multi-locus genetic mapping with pooled sequencing. Updated for Py3",
      author="Matt Edwards, Carson Stacy",
      author_email="matted@mit.edu, clstacy@uark.edu",
      license="MIT",
      url="https://github.com/clstacy/multipool",
      packages=[],
      scripts=["mp_inference.py"],
      zip_safe=True,
      install_requires=["scipy", "numpy"], # pylab is optional; leaving it out for now
  )
