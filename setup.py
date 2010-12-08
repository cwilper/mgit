# bootstrap easy_install
import ez_setup
ez_setup.use_setuptools()

from setuptools import setup

setup(
    name = 'mgit',
    version = '0.1',
    description = "Runs any git command across all repositories beneath a given directory",
    author = "Chris Wilper",
    author_email = "cwilper@gmail.com",
    url = "http://github.com/cwilper/mgit",
    py_modules = ['mgit', 'ez_setup'],
    test_suite = '',
    scripts = ['bin/mgit'],
    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Topic :: Utilities'
    ]
)
