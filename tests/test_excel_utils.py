import pandas as pd
import pytest

from isitmaintained.excel_utils import (
    ExcelData,
    load_excel_data,
    write_excel_data_to_csv,
)


@pytest.mark.skip(reason="Needs fix")
def test_load_excel_data(mocker) -> None:
    mocker.patch("isitmaintained.excel_utils.get_excel_filename", return_value="test.xlsx")
    mock_read_excel = mocker.patch("pandas.read_excel")
    mock_df = pd.DataFrame({"column1": [1, 2], "column2": ["a", "b"]})
    mock_read_excel.return_value = mock_df

    expected = ExcelData(data=[{"column1": 1, "column2": "a"}, {"column1": 2, "column2": "b"}])
    result = load_excel_data("test_config.yml")

    assert result == expected


def test_write_excel_data_to_csv(tmp_path) -> None:
    excel_data = ExcelData(data=[{"column1": 1, "column2": "a"}, {"column1": 2, "column2": "b"}])
    csv_path = tmp_path / "output.csv"

    write_excel_data_to_csv(excel_data, csv_path)

    expected = pd.DataFrame({"column1": [1, 2], "column2": ["a", "b"]})
    result = pd.read_csv(csv_path)
    pd.testing.assert_frame_equal(result, expected)
