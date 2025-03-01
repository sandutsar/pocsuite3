#!/usr/bin/env python
import os
try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

    def find_packages(where='.'):
        # os.walk -> list[(dirname, list[subdirs], list[files])]
        return [folder.replace(os.sep, ".").strip(".")
                for (folder, _, files) in os.walk(where)
                if "__init__.py" in files]


setup(
    name='pocsuite3',
    version='1.8.7',
    url='http://pocsuite.org',
    description='Open-sourced remote vulnerability testing framework.',
    long_description="""\
Pocsuite3 is an open-sourced remote vulnerability testing and proof-of-concept development framework developed by the Knownsec 404 Team. It comes with a powerful proof-of-concept engine, many nice features for the ultimate penetration testers and security researchers.""",
    keywords='PoC,Exp,Pocsuite',
    author='Knownsec 404 Team',
    author_email='404-team@knownsec.com',
    maintainer='Knownsec 404 Team',
    platforms=['any'],
    license='GPLv2',
    zip_safe=False,
    packages=find_packages(),
    include_package_data=True,
    python_requires='>=3.6',
    entry_points={
        "console_scripts": [
            "pocsuite = pocsuite3.cli:main",
            "poc-console = pocsuite3.console:main"
        ]
    },
    install_requires=[
        "requests",
        "requests-toolbelt",
        "PySocks",
        "urllib3",
        "chardet",
        "termcolor",
        "colorama",
        "prettytable",
        "colorlog",
        "scapy",
        "Faker"
    ],
    extras_require={
        'complete': [
            'pyOpenSSL'
        ],
    }
)
