# cykk-audio-transcriber

`cykk-audio-transcriber` is a Python command-line package for transcribing audio into plain text, subtitles, and optional translated transcripts.

It supports:

- local Whisper inference
- the OpenAI speech API
- subtitle export in `txt`, `srt`, `vtt`, `tsv`, and `json`
- optional DeepL-based translation

## Installation

Install the local Whisper workflow:

```bash
pip install "cykk-audio-transcriber[local]"
```

Install the OpenAI API workflow:

```bash
pip install "cykk-audio-transcriber[api]"
```

Install everything:

```bash
pip install "cykk-audio-transcriber[all]"
```

## Usage

```bash
audiototext recording.mp3 --model small --output-formats txt,srt
```

```bash
audiototext recording.mp3 --api-key $OPENAI_API_KEY --output-formats txt,vtt
```

## Project

GitHub repository: https://github.com/cykk/audiototext-pypi

## Related options

For a browser-based transcription workflow, see [mp3totext.ai](https://mp3totext.ai/).
For an online audio and video transcription workflow, see [transvio.ai](https://transvio.ai/).
