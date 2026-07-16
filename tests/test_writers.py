import json

from audiototext.writers import write_outputs


def test_write_outputs(tmp_path):
    payload = {
        "language": "English",
        "text": "hello world",
        "segments": [
            {"id": 0, "start": 0.0, "end": 1.25, "text": "hello world"},
        ],
    }

    written = write_outputs(payload, tmp_path, "sample", ("txt", "srt", "vtt", "tsv", "json"))
    assert len(written) == 5
    assert (tmp_path / "sample.txt").read_text(encoding="utf-8").strip() == "hello world"
    assert "WEBVTT" in (tmp_path / "sample.vtt").read_text(encoding="utf-8")
    assert "00:00:00,000 --> 00:00:01,250" in (tmp_path / "sample.srt").read_text(encoding="utf-8")
    assert "start\tend\ttext" in (tmp_path / "sample.tsv").read_text(encoding="utf-8")
    loaded = json.loads((tmp_path / "sample.json").read_text(encoding="utf-8"))
    assert loaded["language"] == "English"
