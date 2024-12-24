# IsItMaintained

Scrape various sources using a spreadsheet as an input list of dependencies.

Determine if a dependency is maintained.

(NOT FOR PRODUCTION USE, NOT MAINTAINED)

Developing this project, I hope to learn more about some of these:

- VSCode Profiles
- VSCode Extensions
- Copilot Features
- copilot-debug
- python dependencies and their maintainers
- pytest plugins and their popularity and use

This project will be generated and tailored using Copilot Edits and other AI tools.

## Windows Devs as second-class citizens

I'm using Windows locally so this could be Windows-centric.

Windows Python developers have a challenge for some Python packages, since some are developed with a Mac/Linux-centric focus.

The user elevation system in Windows causes some issues with testing public packages and using temporary folder fixtures.

## uv, virtualenv, Copilot and self-signed certificates

There may be issues with virtualenv, uv, and Copilot behind firewalls and security software.

- Don't use virtualenv, use uv instead
- uv python install might be blocked, `--no-python-downloads` or `UV_PYTHON_DOWNLOADS` might help.
- There are some experimental settings with Copilot which can be set to avoid certificate issues.

## VSCode

### Profiles

The default Python profile does not contain some extensions I use:

## VSCode Extensions

Some extensions I may use:

Copilot (and anything from Microsoft or Github)

Markdownlint: https://github.com/igorshubovych/markdownlint-cli/pull/457#issuecomment-1945283551

```shell
code --list-extensions --profile PythonAI
```

```plaintext
charliermarsh.ruff
donjayamanne.python-environment-manager
github.copilot
github.copilot-chat
github.vscode-pull-request-github
ms-azuretools.vscode-docker
ms-python.debugpy
ms-python.python
ms-python.vscode-pylance
ms-toolsai.jupyter
ms-toolsai.jupyter-keymap
ms-toolsai.jupyter-renderers
ms-toolsai.vscode-jupyter-cell-tags
ms-toolsai.vscode-jupyter-slideshow
ms-vscode-remote.remote-containers
ms-vscode-remote.remote-ssh
ms-vscode-remote.remote-ssh-edit
ms-vscode-remote.remote-wsl
ms-vscode-remote.vscode-remote-extensionpack
ms-vscode.remote-explorer
ms-vscode.remote-server
njpwerner.autodocstring
tamasfe.even-better-toml
```

## Packaging Projects

To me, `uv` is now the `2024` standard for packaging projects.  Although it gets updated too frequently!

https://docs.astral.sh/uv/

UV requires some flags for building.

https://packaging.python.org/en/latest/guides/writing-pyproject-toml/

## Python Install

https://docs.astral.sh/uv/guides/install-python/#getting-started

`py --list-paths`

```plaintext
When searching for a Python version, the following locations are checked:

Managed Python installations in the UV_PYTHON_INSTALL_DIR.
A Python interpreter on the PATH as python, python3, or python3.x on macOS and Linux, or python.exe on Windows.
On Windows, the Python interpreters in the Windows registry and Microsoft Store Python interpreters (see py --list-paths) that match the requested version.
```

https://gregoryszorc.com/docs/python-build-standalone/main/quirks.html

```shell
python.exe -m pip
```

```shell
uv pip install
```

```shell
uv python install 3.11 3.12 3.13
```

https://github.com/willkg/dotfiles/blob/main/dotfiles/bin/uv-python-symlink

Generate a .python-version file.

https://github.com/astral-sh/uv/issues/8135

```shell
uv python pin 3.13
```

## Virtual Environment

```shell
pip install --upgrade --user uv
uv venv
.venv/Scripts/Activate
```

## Dependencies

```shell
uv pip install -r pyproject.toml
```

### Developer - Dependency Install

```shell
uv pip install -r pyproject.toml --all-extras
```

## Formatting

`ruff format .`

Future use, toml formatter:

https://github.com/tox-dev/toml-fmt/tree/main/pyproject-fmt

https://pyproject-fmt.readthedocs.io/en/latest/index.html

I encountered a bug similar to this with ruff.

https://github.com/astral-sh/ruff/issues/6335

https://github.com/astral-sh/ruff-vscode

## Linting

`ruff check .`

https://marketplace.visualstudio.com/items?itemName=charliermarsh.ruff

## Markdown

https://github.com/DavidAnson/markdownlint#optionsconfig

## Nox vs. Tox vs. Invoke vs. Makefile vs. SCons

Eventually uv may come out with a replacement task runner.

Generally I prefer using invoke due to its ability to run non-python code.

For this project will test with nox.

https://nox.thea.codes/en/stable/cookbook.html

https://github.com/tox-dev/tox-uv

https://www.pyinvoke.org/

https://hatch.pypa.io/latest/

https://bluesock.org/~willkg/blog/dev/switch_pyenv_to_uv.html

```shell
uv tool install PACKAGE
uv tool install --with tox-uv tox
```

## Web Scraping and Automation

https://pythonbasics.org/pandas-web-scraping/

https://github.com/scrapy/scrapy

https://playwright.dev/

https://github.com/scrapy-plugins/scrapy-playwright

## Logging

https://github.com/open-telemetry/opentelemetry-python-contrib/tree/main/instrumentation

## Items to Review

- using __main__ convention to allow python -m isitmaintained to run.
Need to check updated pattern for __main__ convention.
- various plugins for pytest
- various plugins for opentelemetry
- pandas pivottablejs, qgrid
- Jupyter debugging in vscode
- copilot-debug in terminal and vscode
- Additional copilot extensions and experimental features

## Pandas

https://github.com/pandas-dev/pandas/blob/main/pandas/plotting/__init__.py

## Resources

https://gist.github.com/ahgraber/9ad4d0086a3f239f7872b7f33ebbe4c5
