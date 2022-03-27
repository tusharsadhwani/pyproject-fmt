from __future__ import annotations

from typing import Optional, cast

from tomlkit.items import Array, Table
from tomlkit.toml_document import TOMLDocument

from .config import Config
from .pep508 import normalize_pep508_array
from .util import order_keys, sorted_array


def fmt_build_system(parsed: TOMLDocument, conf: Config) -> None:
    system = parsed.get("build-system")
    if system is None:
        return

    assert isinstance(system, Table)

    requires = system.get("requires")
    if requires is not None:
        assert isinstance(requires, Array)
        normalize_pep508_array(requires, conf.indent)

    backend_path = system.get("backend-path")
    if backend_path is not None:
        assert isinstance(backend_path, Array)
        sorted_array(backend_path, conf.indent)

    order_keys(system, ("build-backend", "requires", "backend-path"))


__all__ = [
    "fmt_build_system",
]
