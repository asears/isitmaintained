"""Logging utilities for setting up OpenTelemetry logging and instrumentation."""

from collections.abc import Callable
from functools import wraps

from opentelemetry import trace
from opentelemetry.instrumentation.click import ClickInstrumentor
from opentelemetry.instrumentation.system_metrics import SystemMetricsInstrumentor
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor, ConsoleSpanExporter


def setup_logging() -> trace.Tracer:
    """Set up OpenTelemetry logging and instrumentation.

    Returns:
        trace.Tracer: The OpenTelemetry tracer instance.
    """
    trace.set_tracer_provider(TracerProvider())
    tracer = trace.get_tracer(__name__)
    span_processor = BatchSpanProcessor(ConsoleSpanExporter())
    trace.get_tracer_provider().add_span_processor(span_processor)

    # Instrument system metrics and click
    SystemMetricsInstrumentor().instrument()
    ClickInstrumentor().instrument()

    return tracer


def logit(func: Callable, tracer: trace.Tracer = None) -> Callable:
    """Add logging to a function.

    Args:
        func (Callable): The function to be decorated.
        tracer (trace.Tracer): The OpenTelemetry tracer instance.

    Returns:
        Callable: The decorated function with logging.

    Example:
        >>> @logit
        ... def my_function(x):
        ...     return x * 2
        >>> my_function(5)
        10
    """
    if tracer is None:
        tracer = trace.get_tracer(__name__)

    @wraps(func)
    def wrapper(*args: tuple, **kwargs: dict) -> Callable:
        with tracer.start_as_current_span(func.__name__):
            return func(*args, **kwargs)

    return wrapper
