# {{ cookiecutter.project_name }}

{{ cookiecutter.description }}

## Installation

```bash
uv pip install {{ cookiecutter.project_name }}
```

## Development

This project uses hatch for environment management and uv for package management.

```bash
# Create development environment
hatch env create

# Run tests
hatch run test

# Run linters
hatch run lint
```
