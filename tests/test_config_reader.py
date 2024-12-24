from pathlib import Path

import pytest

from isitmaintained.config_reader import get_excel_filename


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


def test_get_excel_filename(config_path, write_config_file, mocker) -> None:
    content = "DEFAULT:\n  source_excel: test.xlsx\n"
    write_config_file(config_path, content)

    expected = "test.xlsx"
    result = get_excel_filename(config_path)

    assert result == expected


def test_get_excel_filename_missing(config_path, write_config_file, mocker) -> None:
    content = "DEFAULT:\n"
    write_config_file(config_path, content)

    with pytest.raises(ValueError):
        get_excel_filename(config_path)


def test_get_excel_filename_default_section(config_path, write_config_file, mocker) -> None:
    content = "DEFAULT:\n  source_excel: ./inputs/Pytest-Plugins_2024.xlsx\n"
    write_config_file(config_path, content)

    expected = "./inputs/Pytest-Plugins_2024.xlsx"
    result = get_excel_filename(config_path)

    assert result == expected


def test_get_excel_filename_no_default_section(config_path, write_config_file, mocker) -> None:
    content = "OTHER:\n  source_excel: test.xlsx\n"
    write_config_file(config_path, content)

    with pytest.raises(ValueError):
        get_excel_filename(config_path)


def test_get_excel_filename_no_excel_filename(config_path, write_config_file, mocker) -> None:
    content = "DEFAULT:\n  OtherKey: OtherValue\n"
    write_config_file(config_path, content)

    with pytest.raises(TypeError):
        get_excel_filename(config_path)


def test_get_excel_filename_empty_config(config_path, write_config_file, mocker) -> None:
    content = ""
    write_config_file(config_path, content)

    with pytest.raises(ValueError):
        get_excel_filename(config_path)


def test_get_excel_filename_no_default_dict(config_path, write_config_file, mocker) -> None:
    content = "DEFAULT: not_a_dict"
    write_config_file(config_path, content)

    with pytest.raises(ValueError):
        get_excel_filename(config_path)
