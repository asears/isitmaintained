"""Config reader."""

from pathlib import Path
from typing import Any

import yaml


def get_config(config_path: str = "config.yml", config_profile: str = "DEFAULT") -> dict[str, Any]:
    """Retrieve the configuration from the given configuration file.

    Args:
        config_path (str): The path to the configuration file. Defaults to 'config.yml'.
        config_profile (str): The configuration profile to retrieve. Defaults to 'DEFAULT'.

    Returns:
        dict: The configuration dictionary.

    Raises:
        ValueError: If the configuration is not found or invalid.
        TypeError: If the configuration is not a dictionary.
    """
    required_keys = ["input_dir", "source_excel", "output_dir", "output_csv"]
    error_msg: str = ""

    with Path.open(config_path) as file:
        config = yaml.safe_load(file)
        if config is None:
            error_msg = "Configuration not found in the configuration file"
            raise ValueError(error_msg)

    if config_profile not in config:
        error_msg = f"{config_profile} section not found in the configuration file"
        raise ValueError(error_msg)
    if not isinstance(config[config_profile], dict):
        error_msg = f"{config_profile} section is not a dictionary"
        raise TypeError(error_msg)
    for key in required_keys:
        if key not in config[config_profile]:
            error_msg = f"{key} not found in the configuration file"
            raise ValueError(error_msg)
    return config[config_profile]
