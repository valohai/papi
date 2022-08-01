# Papi

Papi (short for "Pipeline API") is an experimental Python library for
declaring [Valohai pipelines](https://docs.valohai.com/core-concepts/pipelines/) using an imperative syntax.

## Important note

- The design of the API is subject to change and is currently meant for technical validation only.
- Some parts are currently unimplemented and may disappear altogether.

## Usage

You can install the package [from PyPI](https://pypi.org/project/valohai-papi/): `pip install valohai-papi`.

As documentation is still nonexistent, see the `papi_examples` directory for usage examples.

## Development

In the spirit of experimentation, this package uses Poetry for dependency management and
Dephell for compatibility with classic Python package management.

You should be able to install development dependencies with and `pip install -e .[dev]`.

- To format code, please be sure to run `make format`.
- This package aims to be fully type-valid in Mypy's eyes, too. You can run Mypy and Flake8 with `make lint`.
