# Minimal `cookiecutter` Python Package 

## Introduction

A minimalistic python template for creating python console projects. The projects will come bundled with `pytest`, `tox` and `pyinstaller`. This project can be used to share disparate scripts or create a standalone runnable.

This `cookiecutter` template copies from [cookiecutter-pypackage](https://github.com/audreyfeldroy/cookiecutter-pypackage) created by [Audrey Feldroy](https://github.com/audreyfeldroy) and [Remy Greinhofer](https://github.com/rgreinho)'s [python-cookiecutter](https://github.com/rgreinho/python-cookiecutter).

## Pre-requisites

1. Python >= 3.7
2. Install `pip`
3. Checkout `https://github.com/gautamdivgi/cookiecutter-pypackage-minimal`

## Using the template

1. Create your repository. This document is using `https://github.com/gautamdivgi/message-transformer` as an example.
2. Clone the repository locally

```bash
$ git clone https://github.com/gautamdivgi/message-transformer
```

3. Run `cookiecutter` to generate the project.

```bash
$ cookiecutter --overwrite-if-exists https://github.com/gautamdivgi/cookiecutter-pypackage-minimal 

full_name [John Q Public]: Gautam Divgi
email [john.q.public@github.com]: gautamdivgi@some-random-email.com
repo_name [Git Repo Name]: message-transformer
package_name [message_transformer]: 
project_short_description [Python Boilerplate contains all the boilerplate you need to create a Python package.]: Some completely useless JSON transformation
```

The `repo_name` needs to be the same as the repository name for the git repository. The version used by default `0.0.1`.

4. Test drive the template.

```bash
$ cd message-transformer
$ tox -epy37 test
.... testing should succeed ....

$ make dist
.... A package should be built ....
```

## Features and Limitations

### Limitations

The template does not support docker. It builds a basic python package. It also does not support web services or docs building. Those options have been edited out of the original template. The `bump2version` for version handling is not yet tested either.

All document formats will be changed to `.md` from the original `.rst`.

### What it does

Provides a `pytest` and `tox` environment for building python packages. The `Makefile` will have an option to create a binary using `pyinstaller`.

### `cookiecutter.json` Options

1. `full_name`: Full name of the package creator
2. `email`: Email of the package creator
3. `repo_name`: The repository name in git
4. `package_name`: The main root package
5. `project_short_description`: The project short description

## Upcoming Features

1. Consistent versioning using `bump2version`
2. `pyinstaller` builds for self-contained binaries
3. `docker` builds
4. Publish to a `pip` repository
5. Web services using `Flask` and `gunicorn`
