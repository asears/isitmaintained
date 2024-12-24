"""Config schema."""
from typing import Any

CONFIG_SCHEMA: dict[str, Any] = {
    "type": "object",
    "properties": {
        "DEFAULT": {
            "type": "object",
            "properties": {
                "source_excel": {"type": "string"},
                "output_dir": {"type": "string"},
                "output_csv": {"type": "string"},
            },
            "required": ["source_excel", "output_dir", "output_csv"],
        },
    },
    "required": ["DEFAULT"],
}
