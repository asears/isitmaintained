"""Test logging utils."""

from isitmaintained.logging_utils import logit, setup_logging


def test_setup_logging(mocker):
    mock_get_tracer = mocker.patch("isitmaintained.logging_utils.trace.get_tracer")

    tracer = setup_logging()

    assert tracer is not None
    mock_get_tracer.assert_called_once()


def test_logit_decorator(mocker):
    @logit
    def sample_function(x, y):
        return x + y

    mock_span = mocker.patch("isitmaintained.logging_utils.tracer.start_as_current_span")
    expected = 3

    result = sample_function(1, 2)

    assert result == expected
    mock_span.assert_called_once_with("sample_function")
