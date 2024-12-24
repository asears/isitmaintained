import pytest
from click.testing import CliRunner

from isitmaintained.__main__ import main


@pytest.fixture
def config_path(tmp_path):
    config_file = tmp_path / "test_config.yml"
    config_file.write_text("DEFAULT:\n  source_excel: test.xlsx\n")
    return config_file


@pytest.fixture
def excel_file(tmp_path):
    excel_file = tmp_path / "test.xlsx"
    excel_file.write_text("column1,column2\n1,a\n2,b\n")
    return excel_file


@pytest.mark.integration
def test_main_success(config_path, excel_file, tmp_path) -> None:
    runner = CliRunner()
    output_csv = tmp_path / "output.csv"
    result = runner.invoke(main, ["--config", str(config_path), "--output", str(output_csv)])

    assert result.exit_code == 0
    assert "Successfully wrote Excel data to" in result.output
    assert output_csv.exists()


@pytest.mark.integration
def test_main_failure(config_path, tmp_path) -> None:
    runner = CliRunner()
    output_csv = tmp_path / "output.csv"
    result = runner.invoke(main, ["--config", str(config_path), "--output", str(output_csv)])

    assert result.exit_code != 0
    assert "Error: ExcelFilename not found in the configuration file" in result.output
