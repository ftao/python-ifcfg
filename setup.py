import os
import sys

from setuptools import find_packages, setup

sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

import ifcfg  # noqa


setup(
    name='ifcfg',
    version=ifcfg.__version__,
    description="Python Ifconfig Wrapper for Unix/Linux/MacOSX",
    long_description="Python Ifconfig Wrapper for Unix/Linux/MacOSX",
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
    install_requires=[],
    setup_requires=[],
    entry_points="""
    """,
    namespace_packages=[],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Development Status :: 5 - Production/Stable',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: Implementation :: PyPy',
    ],
)
