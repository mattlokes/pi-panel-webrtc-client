"""What the status screen says, worked out from Controller.status().

No GStreamer here: display.py draws a StatusView, and this half is tested
offline.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class StatusView:
    label: str
    detail: str = ""       # "connecting…", or why the feed is down
    hint: str = ""         # "retrying in 12s"
    spinner: bool = False


def status_view(status: dict[str, Any]) -> StatusView | None:
    """The status screen for |status|; None for a blank screen."""
    state, label = status["state"], status["label"]
    if state == "connecting":
        return StatusView(label, "connecting…", spinner=True)
    if state == "retrying":
        retry = status.get("retry_in")
        return StatusView(label, status.get("error") or "offline",
                          f"retrying in {retry:.0f}s" if retry else "", spinner=True)
    if state == "idle" and status["visible"]:
        return StatusView(label)
    return None
