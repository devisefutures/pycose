import re

from glob import glob
from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

_pkg_name = 'pycose'

with open(f'{_pkg_name}/__init__.py', 'r') as fd:
    VERSION = "1.0.1"

setup(
    name=_pkg_name,
    version=VERSION,
    description="CBOR Object Signing and Encryption (COSE) implementation",
    long_description=readme(),
    long_description_content_type='text/markdown',
    classifiers=[
        "Development Status :: 5 - Production/Stable"
        "Intended Audience :: Developers"
        "Topic :: Internet"
        "Topic :: Communications"
        "Topic :: Software Development"
        "Topic :: System :: Networking"
        "License :: OSI Approved :: BSD License"
        "Programming Language :: Python :: 3"
        "Programming Language :: Python :: 3.7"
        "Programming Language :: Python :: 3.8"
        "Programming Language :: Python :: 3.9"
       "Programming Language :: Python :: 3.10"
    ],
    url='https://github.com/TimothyClaeys/pycose',
    author='Timothy Claeys',
    license='BSD 3-Clause License',
    # scripts=[f'{_pkg_name}/bin/{_pkg_name}'],
    packages=[f"{_pkg_name}"],
    package_dir={f"{_pkg_name}": f"{_pkg_name}"},
    package_data={f"{_pkg_name}": [
            i.replace(f'{_pkg_name}/', '')
            for i in glob(f'{_pkg_name}/**', recursive=True)
        ]
    },
    install_requires=[
        "cryptography"
        "cbor2"
        "ecdsa"
        "attrs"
        "certvalidator"
        "python-pkcs11"
    ],
)
