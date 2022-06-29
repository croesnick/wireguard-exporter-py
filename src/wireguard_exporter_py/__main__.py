"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """Prometheus Wireguard Exporter (Python)."""


if __name__ == "__main__":
    main(prog_name="wireguard-exporter-py")  # pragma: no cover
