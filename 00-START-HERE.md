# START HERE — Voice Workstation, explained from zero

This folder explains **every tool and every setting** in plain language.
You do not need any background to follow it.

> 🎯 **Using this for professional videos?**
> Skip the beginner tour — read **`07-PROFESSIONAL-WORKFLOW.md`** first. It is
> the full production pipeline in the correct order (prepare → train → convert
> → enhance → deliver), with recommended settings, a quality-control checklist
> and a time budget. Come back here for what each control means.
>
> The one-line summary of that file:
> **1.** clean the source audio first → **2.** train at **48000** for video →
> **3.** convert with `rmvpe`, Index rate `0.75` → **4.** enhance separately
> (compressor + limiter) → **5.** export WAV, download, check, deliver.

---

## What you have (4 separate web pages)

When you run the workstation you get **4 public links**. Each one is a different
tool on a different page. They all live at the same time.

| # | Page | What it is for |
|---|------|----------------|
| 1 | **Hub** | Two tools in one page. Fastest way to get a job done. |
| 2 | **Full Applio UI** | The big professional tool: train models, convert, TTS, realtime, more. |
| 3 | **Full SVA UI** | StreamVoiceAnon — the same engine as the Hub's first tab, with every option exposed. |
| 4 | **Music remover** | Strips background music off a voiceover. |

**Not included here:** the *dubbing* tool (translates + re-voices audio, English
↔ Hindi). It is a 5th link, and it is switched off in this run.

---

## The one thing to understand: what does the workstation actually do?

It changes **who is speaking** in an audio file.

- *Applio (RVC)* — you **train** a model on someone's voice first, then that
  model can convert any of your recordings into that voice. Best quality, but
  you need training (10–60 minutes of clean voice).
- *SVA / StreamVoiceAnon* — **no training at all**. You give it a short sample
  of the target voice (a "reference") and it converts immediately. Slightly
  lower quality, zero setup.

Everything else in the UI is about *tuning* that conversion.

---

## The normal workflow (what a beginner actually does)

1. **Have your source audio** — the recording of what you want converted
   (your own voice, a voiceover, etc.).
2. **Have a reference sample** — for SVA: a short clip of the target voice.
   For Applio: a trained model.
3. Open the page, drop the audio in, press the button.
4. Wait. You get a result you can play and download.

For a voiceover that has background music, run **Music remover first**, then
feed the clean vocals into Hub/Applio/SVA.

---

## Which page should I start with?

| I want to… | Use |
|------------|-----|
| Just convert quickly, no setup | **Hub** → StreamVoiceAnon tab |
| Train a voice model | **Applio** → Training tab |
| Best quality from a trained model | **Hub** → Applio (RVC) tab, or Applio → Inference |
| Voice sounds too similar to me (anonymize) | **SVA** or Hub → lower the **Alpha** slider |
| Remove background music first | **Music remover** |
| Text → speech in a trained voice | **Applio** → TTS tab |
| Live voice changing | **Applio** → Realtime tab (mic needed) |
| Mix two trained models | **Applio** → Voice Blender |

---

## Understanding the settings (the short version)

Full explanations live in the per-tool files in this folder. The three
settings you will touch most:

- **Pitch shift (semitones)** — moves the voice up or down. `+12` = one octave
  up, `-12` = one octave down. `0` = unchanged. Use this when the voice sounds
  wrong-pitched for the character.
- **F0 method / Pitch extraction algorithm** — *how* the tool finds the pitch.
  `rmvpe` is the recommended default: fast and accurate. `crepe` is slowest but
  most accurate on hard audio.
- **Index rate** — how strictly the converter is forced to sound like the
  trained voice. `0` = ignore the accent/timbre model, `1` = strictly follow it.
  `0.75` is a normal middle setting.

---

## Files in this folder

| File | Contents |
|------|----------|
| `00-START-HERE.md` | This file |
| `01-HUB.md` | Hub page — every control explained |
| `02-SVA.md` | StreamVoiceAnon page — every control explained |
| `03-APPLIO.md` | Applio page — all 24 tabs explained |
| `04-MUSIC-REMOVER.md` | Music remover + every model explained |
| `05-GLOSSARY.md` | Every term used, defined simply |
| `06-TRAIN-A-MODEL.md` | **Train a voice model from ~10 minutes of voice, then use it in every tool, every session** |
| `07-PROFESSIONAL-WORKFLOW.md` | **🎯 The production pipeline: exact order of stages, recommended settings, QC checklist, time budget** |
| `08-MODELS-AND-FILES.md` | **Which formats you can upload, every model in every tool, and how to tell which file is what** |

---

## The five stages (details in `07-PROFESSIONAL-WORKFLOW.md`)

| Stage | Do this |
|-------|---------|
| **1. PREPARE** | Clean the source audio. Music remover if there's a music bed. |
| **2. TRAIN** | Train the model (sampling rate `48000` for video) and **download it**. |
| **3. CONVERT** | Swap the voice. `rmvpe`, Index rate `0.75`. Use **Batch** for many files. |
| **4. ENHANCE** | Compressor → Limiter → Gain. Save as a preset for consistency. |
| **5. DELIVER** | Export WAV, download the file, run the QC checklist. |

Do them **in that order**. Converting before cleaning, or stacking effects while
converting, are the two mistakes that ruin professional results.

---

## Two workflows worth knowing

**No training needed (fastest):** open **Hub → StreamVoiceAnon tab**, give it a
sample of the target voice, convert. Nothing to set up, nothing to save.

**Train a model (best quality):** about 10 minutes of clean voice gets you a
usable model that you can then use in *Hub, Inference, TTS, Voice Blender and
Realtime* — and re-upload in 30 seconds in any later session. Full step-by-step
walkthrough in **`06-TRAIN-A-MODEL.md`**.

> **Important:** a trained model is wiped when the Kaggle session ends. That
> file includes the download step that makes it permanent — don't skip it.

---

## Important behaviour to know

- **Each page is separate.** A crash on one does not stop the others.
- **First run of any tool is slower** — it downloads its AI model the first
  time it is used. Later runs are fast.
- **Long files take proportionally longer.** A 5-minute file is not 5× a
  1-minute file, but it is noticeably longer.
- **If a page shows an error**, press the button again once — the most common
  cause is the model still downloading.
