"""Is it maintained."""

from pathlib import Path

import click

from isitmaintained.config_reader import get_config
from isitmaintained.excel_utils import load_excel_data, write_excel_data_to_csv
from isitmaintained.scraper import scrape_table_from_url


@click.command()
@click.option("--config", default="config.yml", help="Path to the configuration file.")
@click.option("--output", default="output.csv", help="Path to the output CSV file.")
@click.option("--scrape", is_flag=True, help="Scrape the OpenTelemetry Python documentation.")
def main(config: str, output: str, scrape: bool) -> None:
    """Load Excel data from the configuration file and write it to a CSV file."""
    if scrape:
        scrape_data()
    else:
        process_excel_data(config, output)


def scrape_data() -> None:
    """Scrape the OpenTelemetry Python documentation and save the table."""
    scrape_url = "https://opentelemetry.io/docs/languages/python/"
    table = scrape_table_from_url(scrape_url)
    if table:
        with Path("outputs/scraped.txt").open("w", encoding="utf-8") as file:
            file.write(table)
        click.echo("Successfully scraped the table and wrote to outputs/scraped.txt")
    else:
        click.echo("No table found on the page.")


def process_excel_data(config: str, output: str) -> None:
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
