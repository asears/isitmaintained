"""Is it maintained."""

import click

from isitmaintained.config_reader import get_config
from isitmaintained.excel_utils import load_excel_data, write_excel_data_to_csv


@click.command()
@click.option("--config", default="config.yml", help="Path to the configuration file.")
@click.option("--output", default="output.csv", help="Path to the output CSV file.")
def main(config: str, output: str) -> None:
    """Load Excel data from the configuration file and write it to a CSV file."""
    try:
        excel_data = load_excel_data(config)
        output_dir = get_config(config)["output_dir"]
        output_filename = get_config(config)["output_csv"]
        output = f"{output_dir}/{output_filename}"
        write_excel_data_to_csv(excel_data, output)
        click.echo(f"Successfully wrote Excel data to {output}")
    except ValueError as e:
        click.echo(f"Error: {e}")


if __name__ == "__main__":
    main()
