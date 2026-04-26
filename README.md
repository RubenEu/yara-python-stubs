# yara-python-stubs

[PEP 561](https://peps.python.org/pep-0561/) type stubs for
[`yara-python`](https://github.com/VirusTotal/yara-python) **4.5.5**.

`yara-python` is distributed as a C extension and ships without type
information. This package provides the corresponding `.pyi` files so that
`mypy`, `pyright`, `pylance`, and other static analyzers can resolve the
`yara` module's API: classes (`Rules`, `Rule`, `Match`, `StringMatch`,
`StringMatchInstance`), module-level functions (`compile`, `load`,
`set_config`), constants (`CALLBACK_*`, `YARA_VERSION`, ...) and exceptions
(`Error`, `SyntaxError`, `TimeoutError`, `WarningError`).

## Installation

```bash
pip install yara-python-stubs
```

The stubs are picked up automatically by any PEP 561-compliant type checker
once installed in the same environment as `yara-python`. No imports or
configuration changes are required in your code.

To install both the runtime library and these stubs together:

```bash
pip install "yara-python-stubs[runtime]"
```

## Usage

```python
import yara

rules: yara.Rules = yara.compile(
    source='rule example { strings: $a = "foo" condition: $a }'
)

matches: list[yara.Match] = rules.match(data=b"foobar")
for match in matches:
    print(match.rule, match.tags, match.meta)
    for string in match.strings:
        for instance in string.instances:
            print(instance.offset, instance.matched_data)
```

## Versioning

Versions track upstream `yara-python` (`MAJOR.MINOR.PATCH`) plus an extra
component (`.N`) for revisions of the stubs themselves. `4.5.5` corresponds
to `yara-python` 4.5.5.

## License

Apache License 2.0 — see [`LICENSE`](LICENSE).

The stubs are an independent reimplementation of the public Python API of
`yara-python`; this package does not include any code from upstream.
