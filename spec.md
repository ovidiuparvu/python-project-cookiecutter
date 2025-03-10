# Specification

In order to make it easier and faster than it is usually to create a new library or CLI Python project please implement a Python package [cookiecutter](https://www.cookiecutter.io/).

The cookiecutter should use:

1. [hatch](https://hatch.pypa.io/dev/) for Python package and virtual environments management.
2. [uv](https://docs.astral.sh/uv/) for Python package management.
3. [ruff](https://docs.astral.sh/ruff/) for linting and formatting.
4. [mypy](https://mypy.readthedocs.io/en/stable/index.html) for type checking.
5. [pylint](https://github.com/pylint-dev/pylint) for linting.
6. [pytest](https://docs.pytest.org/en/stable/) for testing.
7. [pypgrade](https://pypi.org/project/pyupgrade/) for upgrading to newer Python language syntax.
8. [typer](https://typer.tiangolo.com/) and [rich](https://github.com/Textualize/rich) for CLI applications.
