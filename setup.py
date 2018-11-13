#!/usr/bin/env python
from os.path import join
from setuptools import setup
import releazit

pkg = releazit.__name__

version = releazit.get_version(pkg)

setup(
    name=pkg,
    script_name=pkg,
    version=version,
    author='Vlad Saveliev',
    author_email='vladislav.sav@gmail.com',
    description='Small utility to version and release your tools',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    url='https://github.com/vladsaveliev/' + pkg,
    license='GPLv3',
    packages=[pkg],
    include_package_data=True,
    zip_safe=False,
    install_requires=releazit.get_reqs(),
    scripts=[join('scripts', pkg)],
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
