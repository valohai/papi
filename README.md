# Papi

Papi (short for "Pipeline API") is an experimental Python library for
declaring [Valohai pipelines](https://docs.valohai.com/core-concepts/pipelines/) using an imperative syntax.

## Important note

- The design of the API is subject to change and is currently meant for technical validation only.
- Some parts are currently unimplemented and may disappear altogether.

## Usage

As per the note above, there are no stable distribution versions of Papi just yet.
In the meantime, you can install the package using e.g. `pip install -e git+https://github.com/valohai/papi.git` (or however your Python package manager of choice deals with editable dependencies).

As documentation is still nonexistent, see the `papi_examples` directory for usage examples.

## Development

In the spirit of experimentation, this package uses Poetry for dependency management and
Dephell for compatibility with classic Python package management.

You should be able to install development dependencies both with Poetry and `pip install -e .[dev]`.

- To format code, please be sure to run `poe format`.
- This package aims to be fully type-valid in Mypy's eyes, too. You can run Mypy with `poe check`.
