"""Output writers without whisper runtime dependency."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any


def _format_timestamp(seconds: float, *, srt: bool = False) -> str:
    total_ms = max(0, int(round(seconds * 1000)))
    hours, remainder = divmod(total_ms, 3_600_000)
    minutes, remainder = divmod(remainder, 60_000)
    secs, milliseconds = divmod(remainder, 1000)
    separator = "," if srt else "."
    return f"{hours:02}:{minutes:02}:{secs:02}{separator}{milliseconds:03}"


def _write_txt(result_payload: dict[str, Any], output_path: Path) -> None:
    output_path.write_text(f"{result_payload['text']}\n", encoding="utf-8")


def _write_vtt(result_payload: dict[str, Any], output_path: Path) -> None:
    lines = ["WEBVTT", ""]
    for segment in result_payload["segments"]:
        start = segment["start"] + 0.001 if segment["start"] == 0 else segment["start"]
        lines.append(f"{_format_timestamp(start)} --> {_format_timestamp(segment['end'])}")
        lines.append(segment["text"])
        lines.append("")
    output_path.write_text("\n".join(lines), encoding="utf-8")


def _write_srt(result_payload: dict[str, Any], output_path: Path) -> None:
    lines: list[str] = []
    for index, segment in enumerate(result_payload["segments"], start=1):
        lines.append(str(index))
        lines.append(
            f"{_format_timestamp(segment['start'], srt=True)} --> "
            f"{_format_timestamp(segment['end'], srt=True)}"
        )
        lines.append(segment["text"])
        lines.append("")
    output_path.write_text("\n".join(lines), encoding="utf-8")


def _write_tsv(result_payload: dict[str, Any], output_path: Path) -> None:
    lines = ["start\tend\ttext"]
    for segment in result_payload["segments"]:
        start_ms = int(round(segment["start"] * 1000))
        end_ms = int(round(segment["end"] * 1000))
        text = str(segment["text"]).replace("\t", " ").replace("\n", " ")
        lines.append(f"{start_ms}\t{end_ms}\t{text}")
    output_path.write_text("\n".join(lines), encoding="utf-8")


def _write_json(result_payload: dict[str, Any], output_path: Path) -> None:
    output_path.write_text(json.dumps(result_payload, ensure_ascii=False, indent=2), encoding="utf-8")


def write_outputs(result_payload: dict[str, Any], output_dir: Path, output_name: str, formats: tuple[str, ...]) -> list[Path]:
    output_dir.mkdir(parents=True, exist_ok=True)
    written: list[Path] = []
    writers = {
        "txt": _write_txt,
        "vtt": _write_vtt,
        "srt": _write_srt,
        "tsv": _write_tsv,
        "json": _write_json,
    }

    for output_format in formats:
        output_path = output_dir / f"{output_name}.{output_format}"
        writers[output_format](result_payload, output_path)
        written.append(output_path)

    return written
