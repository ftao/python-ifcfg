import os
import sys
from setuptools import setup, find_packages

sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

import ifcfg

setup(
    name='ifcfg',
    version=ifcfg.__version__,
    description="Python Ifconfig Wrapper for Unix/Linux/MacOSX",
    long_description="Python Ifconfig Wrapper for Unix/Linux/MacOSX",
    classifiers=[],
    keywords='',
    author='Original author: BJ Dierkes',
    author_email='info@learningequality.org',
    url='https://github.com/learningequality/python-ifcfg',
    license='BSD',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    test_suite='nose.collector',
    install_requires=[
        ### Required to build documentation
        # "Sphinx >= 1.0",
        ### Required for testing
        # "nose",
        # "coverage",
        ],
    setup_requires=[],
    entry_points="""
    """,
    namespace_packages=[],
)
