"""Excel Utilities."""

from collections.abc import Hashable
from dataclasses import dataclass
from typing import Any

import pandas as pd

from isitmaintained.config_reader import get_excel_filename


@dataclass
class ExcelData:
    """Excel Data class."""

    data: list[dict[Hashable, Any]]


def load_excel_data(config_path: str = "config.yml") -> ExcelData:
    """Load data from the first sheet of the Excel file specified in the configuration.

    Args:
        config_path (str): The path to the configuration file. Defaults to 'config.yml'.

    Returns:
        ExcelData: A data class containing the loaded data.

    """
    excel_filename = get_excel_filename(config_path)
    df = pd.read_excel(excel_filename, sheet_name=0)
    data = df.to_dict(orient="records")
    return ExcelData(data=data)


def write_excel_data_to_csv(excel_data: ExcelData, csv_path: str) -> None:
    """Write the loaded Excel data to a CSV file.

    Args:
        excel_data (ExcelData): The data class containing the loaded data.
        csv_path (str): The path to the CSV file to write.

    """
    df = pd.DataFrame(excel_data.data)
    df.to_csv(csv_path, index=False)
