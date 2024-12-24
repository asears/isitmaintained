from pathlib import Path

import pytest


@pytest.fixture
def config_path(tmp_path):
    config_file = tmp_path / "test_config.yml"
    yield config_file
    config_file.unlink()


@pytest.fixture
def write_config_file():
    def _write_config_file(config_path: Path, content: str) -> None:
        config_path.write_text(content)

    return _write_config_file
