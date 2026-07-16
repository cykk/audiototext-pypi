# cykk-audio-transcriber

This repository contains the PyPI-focused distribution of `audiototext`.

The package provides a command-line workflow for transcribing audio into plain text, subtitles, and optional translated transcripts. The main project homepage lives at `https://github.com/cykk/audiototext`.

## Install

Local Whisper workflow:

```bash
pip install "cykk-audio-transcriber[local]"
```

OpenAI API workflow:

```bash
pip install "cykk-audio-transcriber[api]"
```

Full feature set:

```bash
pip install "cykk-audio-transcriber[all]"
```

## Example

```bash
audiototext interview.mp3 --model small --output-formats txt,srt
```

```bash
audiototext interview.mp3 --api-key $OPENAI_API_KEY --output-formats txt,vtt
```

## Publishing

Build locally:

```bash
python -m pip install -e .[test]
python -m build
python -m twine check dist/*
```

For PyPI presentation, see [README.pypi.md](README.pypi.md).
