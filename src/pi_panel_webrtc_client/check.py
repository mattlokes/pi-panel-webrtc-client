"""Validate a config.toml and exit: the manifest's `[config] check`.

    python3 -m pi_panel_webrtc_client.check PATH

`pi-panel-ctl config check` (and `config import`) runs it. It imports only
the config parser: no GStreamer, no PyGObject, no display, no network.
Exit 0 if the file is good; otherwise print why and exit 1.
"""

from __future__ import annotations

import sys
from pathlib import Path

from .config import Config, ConfigError


def main(argv: list[str] | None = None) -> int:
    args = sys.argv[1:] if argv is None else argv
    if len(args) != 1:
        print("usage: python3 -m pi_panel_webrtc_client.check CONFIG.toml", file=sys.stderr)
        return 2
    path = Path(args[0])
    try:
        config = Config.load(path)
    except ConfigError as exc:
        print(f"config error: {exc}", file=sys.stderr)
        return 1
    print(f"config ok: {path} ({len(config.cameras)} camera(s))")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
