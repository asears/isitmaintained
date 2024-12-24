"""Nox configuration file."""

import nox
from nox.sessions import Session

nox.options.default_venv_backend = "uv|virtualenv"


@nox.session(venv_backend="uv")
def build(session: Session) -> None:
    """Build the project."""
    session.run("uv", "build")


@nox.session
def test(session: Session) -> None:
    """Run the tests."""
    session.install("pytest", "pytest-cov", "pytest-mock", "pytest-xdist")
    session.run(
        "pytest",
        "--cov=isitmaintained",
        "--cov-report=term-missing",
        "--cov-report=xml",
        "--dist=loadscope",
        "--numprocesses=auto",
    )


@nox.session
def clean(session: Session) -> None:
    """Clean the project."""
    session.run("python", "isitmaintained/main.py", "clean-pycache")


@nox.session
def fmt(session: Session) -> None:
    """Format the code."""
    session.install("ruff")
    session.run("ruff", "format", ".")


@nox.session
def isort(session: Session) -> None:
    """Format the code."""
    session.install("ruff")
    session.run("ruff", "check", "--select", "I", ".", "--fix")


@nox.session
def lint(session: Session) -> None:
    """Lint the code."""
    session.install("ruff", "interrogate")
    session.run("ruff", "check", ".")
    session.run("interrogate", ".", "--vv", "--fail-under=90")


@nox.session
def fix(session: Session) -> None:
    """Fix the code using ruff."""
    session.install("ruff")
    session.run("ruff", "check", ".", "--fix")


@nox.session
def integration_test(session: Session) -> None:
    """Run the integration tests."""
    session.install("pytest", "pytest-cov", "pytest-mock", "pytest-xdist")
    session.run(
        "pytest",
        "tests/integration",
        "--cov=isitmaintained",
        "--cov-report=term-missing",
        "--cov-report=xml",
        "--dist=loadscope",
        "--numprocesses=auto",
    )
