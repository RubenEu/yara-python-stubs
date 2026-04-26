"""Type stubs for yara-python 4.5.5 (PEP 561).

API extracted from yara-python.c in upstream version v4.5.5.
"""

from typing import (
    Any,
    Callable,
    Final,
    IO,
    Literal,
    NamedTuple,
    TypedDict,
)

# --- Versions / module-level constants ---------------------------------------

__version__: Final[str]
YARA_VERSION: Final[str]
YARA_VERSION_HEX: Final[int]

CALLBACK_CONTINUE: Final[Literal[0]]
CALLBACK_ABORT: Final[Literal[1]]

CALLBACK_MATCHES: Final[int]
CALLBACK_NON_MATCHES: Final[int]
CALLBACK_ALL: Final[int]
CALLBACK_TOO_MANY_MATCHES: Final[int]

modules: list[str]

# --- Auxiliary type aliases --------------------------------------------------

_ExternalValue = int | float | bool | str
_Externals = dict[str, _ExternalValue]
_Data = bytes | bytearray | memoryview | str

# --- Structured auxiliary types ---------------------------------------------

class RuleString(NamedTuple):
    namespace: str
    rule: str
    string: str

class CallbackDict(TypedDict):
    matches: bool
    rule: str
    namespace: str
    tags: list[str]
    meta: dict[str, int | bool | str]
    strings: list[StringMatch]

# Callback signatures
_MatchCallback = Callable[[CallbackDict], int]
_IncludeCallback = Callable[[str, str, str], str | None]
_ConsoleCallback = Callable[[str], int]
_WarningsCallback = Callable[[int, RuleString], Any]
_ModulesCallback = Callable[[dict[str, Any]], int]

# --- Match-related types -----------------------------------------------------

class StringMatchInstance:
    offset: int
    matched_data: bytes
    matched_length: int
    xor_key: int
    def plaintext(self) -> bytes: ...
    def __repr__(self) -> str: ...
    def __hash__(self) -> int: ...

class StringMatch:
    identifier: str
    instances: list[StringMatchInstance]
    def is_xor(self) -> bool: ...
    def __repr__(self) -> str: ...
    def __hash__(self) -> int: ...

class Match:
    rule: str
    namespace: str
    tags: list[str]
    meta: dict[str, int | bool | str]
    strings: list[StringMatch]
    def __repr__(self) -> str: ...
    def __hash__(self) -> int: ...
    def __eq__(self, other: object) -> bool: ...
    def __ne__(self, other: object) -> bool: ...
    def __lt__(self, other: Match) -> bool: ...
    def __le__(self, other: Match) -> bool: ...
    def __gt__(self, other: Match) -> bool: ...
    def __ge__(self, other: Match) -> bool: ...

# --- Rule / Rules ------------------------------------------------------------

class Rule:
    identifier: str
    tags: list[str]
    meta: dict[str, int | bool | str]
    is_global: bool
    is_private: bool

class Rules:
    warnings: list[str]
    externals: _Externals

    def __iter__(self) -> Rules: ...
    def __next__(self) -> Rule: ...

    def match(
        self,
        filepath: str | None = ...,
        pid: int | None = ...,
        data: _Data | None = ...,
        externals: _Externals | None = ...,
        callback: _MatchCallback | None = ...,
        fast: bool | None = ...,
        timeout: int | None = ...,
        modules_data: dict[str, bytes] | None = ...,
        modules_callback: _ModulesCallback | None = ...,
        warnings_callback: _WarningsCallback | None = ...,
        which_callbacks: int = ...,
        console_callback: _ConsoleCallback | None = ...,
        allow_duplicate_metadata: bool = ...,
    ) -> list[Match]: ...

    def save(
        self,
        filepath: str | None = ...,
        file: IO[bytes] | None = ...,
    ) -> None: ...

    def profiling_info(self) -> dict[str, int]: ...

# --- Module-level functions --------------------------------------------------

def compile(
    filepath: str | None = ...,
    source: str | None = ...,
    file: IO[bytes] | None = ...,
    filepaths: dict[str, str] | None = ...,
    sources: dict[str, str] | None = ...,
    includes: bool | None = ...,
    externals: _Externals | None = ...,
    error_on_warning: bool | None = ...,
    strict_escape: bool | None = ...,
    include_callback: _IncludeCallback | None = ...,
) -> Rules: ...

def load(
    filepath: str | None = ...,
    file: IO[bytes] | None = ...,
) -> Rules: ...

def set_config(
    stack_size: int | None = ...,
    max_strings_per_rule: int | None = ...,
    max_match_data: int | None = ...,
) -> None: ...

# --- Exceptions --------------------------------------------------------------

class Error(Exception): ...
class SyntaxError(Error): ...
class TimeoutError(Error): ...

class WarningError(Error):
    @property
    def warnings(self) -> list[str]: ...
