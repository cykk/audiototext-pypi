# cykk-audio-transcriber

`cykk-audio-transcriber` is a command-line package for transcribing audio into plain text and subtitles, with optional translated transcripts. This repository contains the PyPI-focused distribution of `audiototext`.

## Features

- Transcribe locally with Whisper or through the OpenAI speech API.
- Export transcripts as `txt`, `srt`, `vtt`, `tsv`, or `json`.
- Optionally translate transcripts with DeepL.
- Run the workflow from the `audiototext` command line.

## Requirements

- Python 3.11 or later
- `ffmpeg` installed and available on your `PATH`

## Install

Install the local Whisper workflow:

```bash
pip install "cykk-audio-transcriber[local]"
```

Install the OpenAI API workflow:

```bash
pip install "cykk-audio-transcriber[api]"
```

Install all optional features:

```bash
pip install "cykk-audio-transcriber[all]"
```

## Usage

Local Whisper transcription:

```bash
audiototext interview.mp3 --model small --output-formats txt,srt
```

OpenAI API transcription:

```bash
audiototext interview.mp3 --api-key $OPENAI_API_KEY --output-formats txt,vtt
```

## Output formats

The `--output-formats` option accepts a comma-separated list of: `txt`, `srt`, `vtt`, `tsv`, and `json`.

## Links

- [Main project](https://github.com/cykk/audiototext)
- [PyPI package](https://pypi.org/project/cykk-audio-transcriber/)
- [Issue tracker](https://github.com/cykk/audiototext-pypi/issues)
- [PyPI presentation README](README.pypi.md)

## Related options

For a browser-based transcription workflow, see [mp3totext.io](https://mp3totext.io/).
For online video-to-text transcription, see [mp4totext.ai](https://mp4totext.ai/).
For an online audio and video transcription workflow, see [AnyToTranscript](https://anytotranscript.com/).

## Publishing

Build and validate the package locally:

```bash
python -m pip install -e .[test]
python -m build
python -m twine check dist/*
```
