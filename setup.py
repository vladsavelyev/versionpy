#!/usr/bin/env python
from os.path import join
from setuptools import setup

import versionpy
pkg = versionpy.__name__
version = versionpy.get_version(pkg)

setup(
    name=pkg,
    script_name=pkg,
    version=version,
    author='Vlad Saveliev',
    author_email='vladislav.sav@gmail.com',
    description='Small utility to track and bump the version of your python tool',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url='https://github.com/vladsaveliev/' + pkg,
    license='GPLv3',
    packages=[pkg],
    include_package_data=True,
    zip_safe=False,
    setup_requires=[],
    install_requires=versionpy.get_reqs(),
    scripts=[
        join('scripts', 'bump'),
        join('scripts', 'version'),
        join('scripts', 'increment_version')
    ],
    keywords='bioinformatics',
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX',
        'Operating System :: Unix',
        'Programming Language :: Python',
        'Topic :: Scientific/Engineering',
    ],
)
