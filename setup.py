import os
from setuptools import setup
 
setup(name='python-zonediff',
    version="1.0",
    description='Library and commandline tool to create logical diffs of zonefiles',
    author='Dennis Kaarsemaker',
    author_email='dennis@kaarsemaker.net',
    py_modules=['zonediff'],
    url='http://github.com/seveas/python-zonediff',
    classifiers=[
        "Intended Audience :: Developers",
        "Intended Audience :: System Administrators",
        "Operating System :: OS Independent",
        "Topic :: Internet :: Name Service (DNS)",
        "Topic :: Software Development",
    ],
)
