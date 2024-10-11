# pytia

A wrapper for the catia v5 api.

![state](https://img.shields.io/badge/State-beta-brown.svg?style=for-the-badge)
![version](https://img.shields.io/github/v/release/deloarts/pytia?style=for-the-badge&color=orange)

[![python](https://img.shields.io/badge/Python-3.10-blue.svg?style=for-the-badge)](https://www.python.org/downloads/)
![catia](https://img.shields.io/badge/CATIA-V5%206R2023-blue.svg?style=for-the-badge)
![OS](https://img.shields.io/badge/OS-WIN11-blue.svg?style=for-the-badge)

**pytia** is a wrapper for the CATIA V5 api based on the **V5Automation.chm** help file. It provides some useful utilities and features for interacting with the api and a cli tool. More details: <https://pytia.deloarts.com/>.

Check out the pytia ecosystem:

- **pytia** ([web](https://pytia.deloarts.com/), [repo](https://github.com/deloarts/pytia)): The heart of this project.
- **pytia-property-manager** ([web](https://pytia.deloarts.com/property-manager/v0.html), [repo](https://github.com/deloarts/pytia-property-manager)) : An app to edit part and product properties.
- **pytia-bounding-box** ([web](https://pytia.deloarts.com/bounding-box/v0.html), [repo](https://github.com/deloarts/pytia-bounding-box)): For retrieving the bounding box of a part.
- **pytia-bill-of-material** ([web](https://pytia.deloarts.com/bill-of-material/v0.html), [repo](https://github.com/deloarts/pytia-bill-of-material)): Exports the bill of material and data of a product.
- **pytia-title-block** ([web](https://pytia.deloarts.com/title-block/v0.html), [repo](https://github.com/deloarts/pytia-title-block)): An app to edit a drawing's title block.
- **pytia-quick-export** ([web](https://pytia.deloarts.com/quick-export/v0.html), [repo](https://github.com/deloarts/pytia-quick-export)): Single file export with useful features.
- **pytia-reorder-tree** ([web](https://pytia.deloarts.com/reorder-tree/v0.html), [repo](https://github.com/deloarts/pytia-reorder-tree)): Brings order in your product graph tree.
- **pytia-ui-tools** ([web](https://pytia.deloarts.com/), [repo](https://github.com/deloarts/pytia-ui-tools)): A toolbox for all pytia apps.

Table of contents:

- [pytia](#pytia)
  - [1 installation](#1-installation)
    - [1.1 system requirements](#11-system-requirements)
    - [1.2 pip](#12-pip)
      - [1.2.1 pip from wheel](#121-pip-from-wheel)
      - [1.2.2 ssh](#122-ssh)
    - [1.3 setup](#13-setup)
      - [1.3.1 environment variables](#131-environment-variables)
      - [1.3.2 catia environment file](#132-catia-environment-file)
    - [1.4 troubleshooting](#14-troubleshooting)
  - [2 usage](#2-usage)
    - [2.1 commands](#21-commands)
    - [2.2 options](#22-options)
  - [3 developing](#3-developing)
    - [3.1 repository](#31-repository)
      - [3.1.1 cloning](#311-cloning)
      - [3.1.2 main branch protection](#312-main-branch-protection)
      - [3.1.3 branch naming convention](#313-branch-naming-convention)
      - [3.1.4 issues](#314-issues)
    - [3.2 poetry](#32-poetry)
      - [3.2.1 setup](#321-setup)
      - [3.2.2 install](#322-install)
      - [3.2.3 tests](#323-tests)
      - [3.2.4 build](#324-build)
    - [3.3 insides](#33-insides)
      - [3.3.1 wrapper](#331-wrapper)
      - [3.3.2 helper](#332-helper)
      - [3.3.3 utilities](#333-utilities)
      - [3.3.4 logging](#334-logging)
      - [3.3.5 exceptions](#335-exceptions)
    - [3.4 pre-commit hooks](#34-pre-commit-hooks)
    - [3.5 docs](#35-docs)
    - [3.6 new revision checklist](#36-new-revision-checklist)
  - [4 license](#4-license)
  - [5 changelog](#5-changelog)
  - [6 to do](#6-to-do)

## 1 installation

### 1.1 system requirements

- Windows 11
- CATIA V5 6R-2023
- [Python 3.10](https://www.python.org/downloads/)

> ✏️ These requirements aren't strict, you can use **pytia** on older or more recent systems, but it isn't tested on these.

### 1.2 pip

PYTIA isn't available on PyPi, but you still can install it via pip. Here are two options, choose the one you like best:

#### 1.2.1 pip from wheel

If you want to install PYTIA from the published wheel file, use:

```powershell
python -m pip install https://github.com/deloarts/pytia/releases/download/v0.4.0/pytia-0.4.0-py3-none-any.whl
```

This command installs PYTIA v0.4.0.

#### 1.2.2 ssh

Create a [ssh key and add it to your github account](https://docs.github.com/en/authentication/connecting-to-github-with-ssh) for access. Make sure your ssh key is working:

```powershell
ssh -T git@github.com
```

```powershell
python -m pip install git+ssh://git@github.com/deloarts/pytia.git
```

This command installs the latest stable version of PYTIA.

If you're using poetry add this to you **pyproject.toml** file:

```toml
[tool.poetry.dependencies]
pytia = { git = "ssh://git@github.com/deloarts/pytia.git", branch="main" }
```

### 1.3 setup

#### 1.3.1 environment variables

By default you don't have to add any environment variables to your system. The following table lists what they are used for. To add the environment variables to your system open the PowerShell and enter the command like this:

```powershell
set ENV_VAR=ENV_VALUE
```

| | ENV_VAR | ENV_VALUE | Default | Description |
| --- | --- | --- | --- | --- |
| 1 | PYTIA_NO_PROPS | 0 or 1 | 0 | By default pytia will create user ref properties (pytia version, etc.) inside a CATPart/CATProduct. If you don't want this set this variable to 1. |
| 2 | PYTIA_IGNORE_BOM_ERROR | 0 or 1 | 0 | By default no errors are ignored. But the BOM export keeps failing you can try it again with this parameter set to 1. |

#### 1.3.2 catia environment file

For some utilities you may want to setup your CATIA environment file according to the following table:

| | ENV_VAR | ENV_VALUE | Description |
| --- | --- | --- | --- |
| 1 | DEACTIVATE_SHEETMETAL_WARNING_AT_PART_OPEN | Yes | If you use a stack export and you have some parts designed in the sheet metal environment you may want to set this variable. Otherwise you will get a warning at every opening of an sheet metal part document. |

### 1.4 troubleshooting

There are some things to be aware of:

- Depending on the version of pytia it may be required to install the Microsoft C++ Build Tools in order to install **pytia**. Check the installation output for more details.
- If you try to install **pytia** globally it can be required to run the post installation script for the *pywin32* dependency. To do so, navigate to your python installation directory and enter the `Scripts` directory (default: `%LOCALAPPDATA%\Programs\Python\Python310\Scripts\`). Then run the following command with admin rights: `python pywin32_postinstall.py -install`. This isn't necessary if you install pytia in a virtual environment.

## 2 usage

Once installed you can use **pytia** as a python module with a cli:

```powershell
python -m pytia
```

This generates the following output:

```plain
PYTIA 0.4.0

Usage: python -m pytia [OPTIONS] COMMAND [ARGS]...

  Command line tool for CATIA V5.

Options:
  --verbose  Show detailed logging info.
  --help     Show this message and exit.

Commands:
  bom     Exports the bill of material for the current product.
  box     Retrieves the bounding box for the current part.
  mirror  Creates a mirrored version of the current CATPart.
  new     Creates a new document (part or product).

See the full output in C:\Users\...\AppData\Local\Temp\pytia.log
```

### 2.1 commands

Above you can see all available commands:

- bom: *Exports the bill of material for the current product.*
- box: *Retrieves the bounding box for the current part.*
- mirror: *Creates a mirrored version of the current CATPart.*
- new: *Creates a new document (part or product).*

Use those commands the following way:

```powershell
python -m pytia box
```

This will create the following sample output:

```powershell
PYTIA 0.4.0

[ INFO ]  Bounding box of the current part:
          X = 100.0mm
          Y = 80.0mm
          Z = 20.0mm

See the full output in C:\Users\...\AppData\Local\Temp\pytia.log
```

### 2.2 options

Use an option to alter the behavior of the output:

- --verbose: *Prints the logging messages to standard output.*
- --help: *Shows helpful information.*

Those options can be used on a global level, or on a specific command:

```powershell
python -m pytia --verbose
```

```powershell
python -m pytia box --verbose
```

## 3 developing

For developing you would, additionally to the system requirements, need to install:

- [Poetry](https://python-poetry.org/docs/master/#installation)
- [Git](https://git-scm.com/downloads) or [GitHub Desktop](https://desktop.github.com/)

### 3.1 repository

#### 3.1.1 cloning

Clone the repo to your local machine:

```powershell
cd $HOME
New-Item -Path '.\git\pytia' -ItemType Directory
cd .\git\pytia\
git clone git@github.com:deloarts/pytia.git
```

Or use GitHub Desktop.

#### 3.1.2 main branch protection

> ❗️ Never develop new features and fixes in the main branch!

The main branch is protected: it's not allowed to make changes directly to it. Create a new branch in order work on issues. The new branch should follow the naming convention from below.

#### 3.1.3 branch naming convention

1. Use grouping tokens at the beginning of your branch names, such as:
    - feature: A new feature that will be added to the project
    - fix: For bugfixes
    - tests: Adding or updating tests
    - docs: For updating the docs
    - wip: Work in progress, won't be finished soon
    - junk: Just for experimenting
2. Use slashes `/` as delimiter in branch names (`feature/docket-export`)
3. Avoid long descriptive names, rather refer to an issue
4. Do not use bare numbers as leading parts (`fix/108` is bad, `fix/issue108` is good)

#### 3.1.4 issues

Use the issue templates for creating an issue. Please don't open a new issue if you haven't met the requirements and add as much information as possible. Further:

- Format your code in an issue correctly with three backticks, see the [markdown guide](https://docs.github.com/en/get-started/writing-on-github/getting-started-with-writing-and-formatting-on-github/basic-writing-and-formatting-syntax).
- Add the full error trace.
- Do not add screenshots for code or traces.

### 3.2 poetry

#### 3.2.1 setup

If you prefer the environment inside the projects root, use:

```powershell
poetry config virtualenvs.in-project true
```

> ⚠️ Make sure not to commit the virtual environment to GitHub. See [.gitignore](.gitignore) to find out which folders are ignored.

#### 3.2.2 install

Install all dependencies (assuming you are inside the projects root folder):

```powershell
poetry install
```

Check your active environment with:

```powershell
poetry env list
poetry env info
```

Update packages with:

```powershell
poetry update
```

#### 3.2.3 tests

Tests are done with pytest. For testing with poetry run:

```powershell
poetry run pytest
```

> ⚠️ Test discovery in VS Code only works when CATIA is running.

#### 3.2.4 build

```powershell
poetry build
```

This exports the module to the [dist](/dist/) folder.

> ⚠️ Make sure not to commit dev-builds (the dist folder isn't ignored, because this package isn't published on pip yet).

### 3.3 insides

#### 3.3.1 wrapper

The [wrapper](/pytia/wrapper/) folder contains wrapping classes for the framework. Those classes provide basic needs, like checking for existing objects, creating objects, ...

#### 3.3.2 helper

The [helper](/pytia/helper/) folder contains mainly helper functions for the wrapper and the utilities.
> ⚠️ Some helper functions are currently a huge mess

#### 3.3.3 utilities

The [utilities](/pytia/utilities/) folder provides utility functions which are intended to be used in other projects, like retrieving the bounding box of a part or exporting a bill of material.

Some utilities can be used as keyword arguments. To inspect it:

```powershell
python -m pytia --help
```

#### 3.3.4 logging

You can use the [log.py](/pytia/log.py) module to log messages directly to the **pytia** logger:

```python
from pytia.log import log
log.info("This is an info log")
```

You can also use the predefined stream- and file-handler:

```python
log.add_stream_handler()
log.add_file_handler()
```

If you want to use your own logger you can access the **pytia** logger via its name:

```python
import logging
logger = logging.getLogger("pytia")
```

You can then add custom handlers and formats to the logger, so it fits your needs:

```python
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger.setFormatter(formatter)
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
logger.addHandler(formatter)
```

#### 3.3.5 exceptions

Pytia exceptions are defined in the [exceptions.py](/pytia/exceptions.py) file. All raised exceptions inside pytia have their roots here. All exceptions from this module will be logged to the **pytia** logger as error messages with a traceback.

### 3.4 pre-commit hooks

Don't forget to install the pre-commit hooks:

```powershell
pre-commit install
```

### 3.5 docs

Documentation is done with [pdoc3](https://pdoc3.github.io/pdoc/).

To update the documentation run:

```powershell
python -m pdoc --html --output-dir docs pytia
```

For preview run:

```powershell
python -m pdoc --http : pytia
```

> ⚠️ Creating the documentation requires CATIA to be running.

### 3.6 new revision checklist

1. Update **dependencies**: `poetry update`
2. Update the **version** in
   - [pyproject.toml](pyproject.toml)
   - [__ init __.py](pytia/__init__.py)
   - [README.md](README.md)
3. Run all **tests**: `poetry run pytest`
4. Check **pylint** output: `poetry run pylint pytia/`
5. Update the **documentation**: `poetry run pdoc --force --html --output-dir docs pytia`
6. Update the **lockfile**: `poetry lock`
7. Update the **requirements.txt**: `poetry export --with dev -f requirements.txt -o requirements.txt`
8. **Build** the package: `poetry build`

## 4 license

[MIT License](LICENSE)

## 5 changelog

[**v0.4.0**](https://github.com/deloarts/pytia/releases/tag/v0.4.0): Add path utils.  
[**v0.3.5**](https://github.com/deloarts/pytia/releases/tag/v0.3.5): Bump deps version.  
[**v0.3.4**](https://github.com/deloarts/pytia/releases/tag/v0.3.4): Fix material wrapper.  
[**v0.3.3**](https://github.com/deloarts/pytia/releases/tag/v0.3.3): Fix uncaught parameter error.  
[**v0.3.2**](https://github.com/deloarts/pytia/releases/tag/v0.3.2): Update pywin32 dependency.  
[**v0.3.1**](https://github.com/deloarts/pytia/releases/tag/v0.3.1): Update console methods.  
[**v0.3.0**](https://github.com/deloarts/pytia/releases/tag/v0.3.0): Add dependency [`pycatia`](https://github.com/evereux/pycatia).  
[**v0.2.5**](https://github.com/deloarts/pytia/releases/tag/v0.2.5): Remove dependency `py`.  
[**v0.2.4**](https://github.com/deloarts/pytia/releases/tag/v0.2.4): Fix `get_tolerances` method.  
[**v0.2.3**](https://github.com/deloarts/pytia/releases/tag/v0.2.3): Update mako.  
[**v0.2.2**](https://github.com/deloarts/pytia/releases/tag/v0.2.2): Use pathlib instead of str.  
[**v0.2.1**](https://github.com/deloarts/pytia/releases/tag/v0.2.1): Add docket generator.  
[**v0.2.0**](https://github.com/deloarts/pytia/releases/tag/v0.2.0): Add drawing document wrapper.  
[**v0.1.1**](https://github.com/deloarts/pytia/releases/tag/v0.1.1): Add `delete` method to the properties wrapper.  
[**v0.1.0**](https://github.com/deloarts/pytia/releases/tag/v0.1.0): Initial commit.  

## 6 to do

Using VS Code [Comment Anchors](https://marketplace.visualstudio.com/items?itemName=ExodiusStudios.comment-anchors) to keep track of to-dos.
