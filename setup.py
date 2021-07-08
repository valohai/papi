# -*- coding: utf-8 -*-

# DO NOT EDIT THIS FILE!
# This file has been autogenerated by dephell <3
# https://github.com/dephell/dephell

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

readme = ""

setup(
    long_description=readme,
    name="valohai-papi",
    version="0.1.2",
    description="Experimental imperative Valohai pipeline API",
    python_requires="==3.*,>=3.6.1",
    project_urls={"homepage": "https://github.com/valohai/papi"},
    author="Aarni Koskela",
    author_email="aarni@valohai.com",
    license="MIT",
    packages=["papi"],
    package_dir={"": "."},
    package_data={"papi": ["*.typed"]},
    install_requires=[
        'dataclasses>=0.6; python_version < "3.7"',
        "valohai-yaml>=0.14.1",
    ],
    extras_require={
        "dev": [
            "black==20.*,>=20.8.0.b1",
            "dephell==0.*,>=0.8.3",
            "flake8==3.*,>=3.9.0",
            "flake8-bugbear==21.*,>=21.4.3",
            "flake8-print==4.*,>=4.0.0",
            "flake8-return==1.*,>=1.1.2",
            "flake8-simplify==0.*,>=0.14.0",
            "isort==5.*,>=5.8.0",
            "mypy==0.*,>=0.812.0",
            "poethepoet==0.*,>=0.10.0",
        ]
    },
)
