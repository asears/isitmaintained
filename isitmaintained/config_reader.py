"""Config reader."""

from pathlib import Path

import yaml


def get_excel_filename(config_path: str = "config.yml") -> str:
    """Retrieve the Excel filename from the given configuration file.

    Args:
        config_path (str): The path to the configuration file. Defaults to 'config.yml'.

    Returns:
        str: The Excel filename specified in the configuration file.

    Raises:
        ValueError: If 'ExcelFilename' is not found in the configuration file.
        TypeError: If the 'DEFAULT' section is not a dictionary.

    """
    error_msg: str = ""
    with Path.open(config_path, encoding="utf-8") as file:
        config = yaml.safe_load(file)
        if config is None:
            error_msg = "source_excel not found in the configuration file"
            raise ValueError(error_msg)

    if "DEFAULT" not in config:
        error_msg = "DEFAULT section not found in the configuration file"
        raise ValueError(error_msg)
    if not isinstance(config["DEFAULT"], dict):
        error_msg = "DEFAULT section is not a dictionary"
        raise TypeError(error_msg)
    if "source_excel" not in config["DEFAULT"]:
        error_msg = "ExcelFilename not found in the configuration file"
        raise ValueError(error_msg)
    return str(config["DEFAULT"]["source_excel"])
