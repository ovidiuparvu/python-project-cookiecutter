{%- if cookiecutter.create_cli == "yes" %}
"""CLI entry point for {{ cookiecutter.project_name }}."""

import typer
from rich import print

app = typer.Typer()

@app.command()
def main() -> None:
    """Main CLI entry point."""
    print("[bold green]Hello from {{ cookiecutter.project_name }}![/bold green]")

if __name__ == "__main__":
    app()
{%- endif %}
