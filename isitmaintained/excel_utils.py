"""Excel Utilities."""

from collections.abc import Hashable
from dataclasses import dataclass
from typing import Any

import pandas as pd

from isitmaintained.config_reader import get_config
from isitmaintained.logging_utils import logit


@dataclass
class ExcelData:
    """Excel Data class."""

    data: list[dict[Hashable, Any]]


@logit
def load_excel_data(config_path: str = "config.yml") -> ExcelData:
    """Load data from the first sheet of the Excel file specified in the configuration.

    Args:
        config_path (str): The path to the configuration file. Defaults to 'config.yml'.

    Returns:
        ExcelData: A data class containing the loaded data.

    """
    input_folder = get_config(config_path)["input_dir"]
    input_filename = get_config(config_path)["source_excel"]
    full_path = f"{input_folder}/{input_filename}"
    df = pd.read_excel(full_path, sheet_name=0)
    data = df.to_dict(orient="records")
    return ExcelData(data=data)


@logit
def write_excel_data_to_csv(excel_data: ExcelData, csv_path: str) -> None:
    """Write the loaded Excel data to a CSV file.

    Args:
        excel_data (ExcelData): The data class containing the loaded data.
        csv_path (str): The path to the CSV file to write.

    """
    df = pd.DataFrame(excel_data.data)
    df.to_csv(csv_path, index=False)
