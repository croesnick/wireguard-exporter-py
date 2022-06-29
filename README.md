# Prometheus Wireguard Exporter (Python)

[![PyPI](https://img.shields.io/pypi/v/wireguard-exporter-py.svg)][pypi_]
[![Status](https://img.shields.io/pypi/status/wireguard-exporter-py.svg)][status]
[![Python Version](https://img.shields.io/pypi/pyversions/wireguard-exporter-py)][python version]
[![License](https://img.shields.io/pypi/l/wireguard-exporter-py)][license]

[![Read the documentation at https://wireguard-exporter-py.readthedocs.io/](https://img.shields.io/readthedocs/wireguard-exporter-py/latest.svg?label=Read%20the%20Docs)][read the docs]
[![Tests](https://github.com/croesnick/wireguard-exporter-py/workflows/Tests/badge.svg)][tests]
[![Codecov](https://codecov.io/gh/croesnick/wireguard-exporter-py/branch/main/graph/badge.svg)][codecov]

[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)][pre-commit]
[![Black](https://img.shields.io/badge/code%20style-black-000000.svg)][black]

[pypi_]: https://pypi.org/project/wireguard-exporter-py/
[status]: https://pypi.org/project/wireguard-exporter-py/
[python version]: https://pypi.org/project/wireguard-exporter-py
[read the docs]: https://wireguard-exporter-py.readthedocs.io/
[tests]: https://github.com/croesnick/wireguard-exporter-py/actions?workflow=Tests
[codecov]: https://app.codecov.io/gh/croesnick/wireguard-exporter-py
[pre-commit]: https://github.com/pre-commit/pre-commit
[black]: https://github.com/psf/black

## Features

Fetches Wireguard statistics from current running process by invoking `wg show <iface> dump`.
Currently, two gauges are exposes: whether executing and parsing the above command succeeded, and the number of current open connections.

## Requirements

Python >=3.9.

## Installation

You can install _Prometheus Wireguard Exporter (Python)_ from this repo via [pip].

### Docker

Build the image

```shell
docker build -t wireguard-exporter .
```

and run it with

```shell
docker run -d --net=host --cap-add=NET_ADMIN wireguard-exporter
```

## Usage

Please see the [Command-line Reference] for details.

## Alternatives

This exporter is merely a sample how to use the Prometheus Python client to build your own exporter. 😊
It is far from exposing all relevant Wireguard metrics.

If you want a more complete exporter, try, for instance, <https://github.com/MindFlavor/prometheus_wireguard_exporter>.

## Contributing

Contributions are very welcome.
To learn more, see the [Contributor Guide].

## License

Distributed under the terms of the [MIT license][license],
_Prometheus Wireguard Exporter (Python)_ is free and open source software.

## Issues

If you encounter any problems,
please [file an issue] along with a detailed description.

## Credits

This project was generated from [@cjolowicz]'s [Hypermodern Python Cookiecutter] template.

[@cjolowicz]: https://github.com/cjolowicz
[pypi]: https://pypi.org/
[hypermodern python cookiecutter]: https://github.com/cjolowicz/cookiecutter-hypermodern-python
[file an issue]: https://github.com/croesnick/wireguard-exporter-py/issues
[pip]: https://pip.pypa.io/

<!-- github-only -->

[license]: https://github.com/croesnick/wireguard-exporter-py/blob/main/LICENSE
[contributor guide]: https://github.com/croesnick/wireguard-exporter-py/blob/main/CONTRIBUTING.md
[command-line reference]: https://wireguard-exporter-py.readthedocs.io/en/latest/usage.html
