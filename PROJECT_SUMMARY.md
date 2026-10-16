# Project Summary — Persistent Voice Conversion Workstation

One-paragraph version: a self-contained, GPU-backed voice studio that runs on
Kaggle. You attach one dataset, paste one cell, and get public web URLs for
converting, training, and dubbing voices — no install on your PC, works from a
phone.

---

## What it is

A Kaggle-hosted workstation for voice work. Everything (code, models, UIs)
ships inside a single Kaggle dataset; a one-cell script rebuilds the
environment each session and prints public `https://….gradio.live` links you
open on any device.

## The five tools (each is its own URL)

| # | Tool | Port | What it does | Switch |
|---|------|------|--------------|--------|
| 1 | **Hub (quick convert)** | 7860 | One page with both engines for fast jobs | `ENABLE_HUB` |
| 2 | **Full Applio UI** | 7861 | Train a voice model, inference, TTS, realtime, voice blender | `ENABLE_APPLIO` |
| 3 | **Full SVA UI** | 7862 | StreamVoiceAnon zero-shot voice cloning (no training) | `ENABLE_SVA` |
| 4 | **Music remover** | 7863 | Strips background music before conversion | `ENABLE_MUSIC_REMOVER` |
| 5 | **Dubbing (SoniTranslate)** | 7864 | Translates audio, re-speaks it in your voice (English ↔ Hindi) | `ENABLE_DUBBING` |

Each switch is `True`/`False` at the top of `ONE_CELL.py`. `True` starts that
tool *and* installs its libraries; `False` skips it entirely (faster startup).
The three core tools ship `True`; the two extras ship `False`.

## How the pieces fit

```
Kaggle notebook (GPU T4 x2)
  └── ONE_CELL.py            sets env switches, finds + runs the launcher
        └── launch_workstation.py   (in the dataset)
              ├── bootstrap_v4.py   installs deps, patches UIs, builds venvs
              └── starts each enabled UI, each on its own port + share tunnel
```

- **One dataset** holds all code + models (`voice-conversion-workstation`).
- **One venv per tool** so incompatible pins never break each other (the
  dubbing UI needs `gradio 4.19.2`; the others use `gradio 5.23`/`6.20`).
- **Each UI gets its own public tunnel**, so a failure in one never takes down
  the rest.

## Why it's split across venvs

The dubbing tool (SoniTranslate) pins `gradio==4.19.2` and
`transformers<=4.39.3`. SVA needs `gradio 5.23.0` / `transformers 4.46.3`. Those
are mutually exclusive, so dubbing runs in its own isolated environment on its
own port. Same reason it is a separate URL and not a tab inside the others.

## Current state (proven 2026-10-08)

- All five tools boot and serve; live dubbing UI verified with all probes green.
- The one-cell flow works from a **brand-new Kaggle account**: upload the
  workstation `.zip` as a dataset on the website (Kaggle unpacks it), attach it,
  and a verbatim `ONE_CELL.py` run published all core URLs (HTTP 200 from
  outside Kaggle) — tested on both CPU and T4×2.
- Every `.py` compiles clean; the local backup zip matches the live tree
  exactly; file pickers accept audio + video; YouTube download and rate-limit
  paths are hardened.

## Files here

| File | Role |
|------|------|
| `ONE_CELL.py` | The one notebook cell you run every session |
| `NEW_ACCOUNT_UPLOAD.sh` | Optional terminal alternative to the browser upload |
| `README.md` | Step-by-step how-to |
| `PROJECT_SUMMARY.md` | This file |

## User documentation

The **`../GUIDES/`** folder is the full manual (9 files, ~1,800 lines):

| File | Covers |
|------|--------|
| `00-START-HERE.md` | What each tool is, the 5-stage pipeline |
| `01-HUB.md` → `04-MUSIC-REMOVER.md` | Every control of every tool, explained |
| `05-GLOSSARY.md` | A–Z of every term |
| `06-TRAIN-A-MODEL.md` | Train a voice from ~10 min of audio, reuse it every session |
| `07-PROFESSIONAL-WORKFLOW.md` | The production pipeline in order + QC checklist + time budget |
| `08-MODELS-AND-FILES.md` | Upload formats, every model, and which file is what |

Operational history for maintainers lives in `agency/DEV_HANDOFF.md`.
