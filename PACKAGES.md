# System packages

Measured on a fresh Raspberry Pi OS Lite (trixie, arm64) on a Pi 5, with
pi-panel-core already installed and `--no-install-recommends`. They match
`[system]` in `pi-panel.toml`.

```
python3-gi
python3-gst-1.0                 # gst-python overrides: without them promise replies crash
python3-gi-cairo                # the status screen is drawn with Cairo
gir1.2-pango-1.0                # Pango / PangoCairo typelibs
gir1.2-gst-plugins-bad-1.0      # GstWebRTC / GstSdp typelibs
gstreamer1.0-plugins-bad        # webrtcbin, waylandsink, h265parse, v4l2slh265dec
gstreamer1.0-plugins-good       # rtph264depay, rtph265depay, cairooverlay
gstreamer1.0-libav              # avdec_h264 / avdec_h265
gstreamer1.0-nice               # ICE for webrtcbin
```

**This is heavy: about 234 packages**, even without Recommends. Nearly all are
hard Depends of `gstreamer1.0-plugins-bad` and `gstreamer1.0-libav` (ffmpeg,
onnxruntime, codec and audio libraries, and GTK 3). The image should keep it
optional.

## Other requirements

- **Kernel ≥ 6.18** for `v4l2slh265dec` (the Pi 5's HEVC block, `/dev/video19`). H.264 is always decoded in software by `avdec_h264`: the Pi 5 has no H.264 block.
- It runs on the system `/usr/bin/python3`, with no venv and no uv. pi-panel-varlink is found through `PYTHONPATH`.
