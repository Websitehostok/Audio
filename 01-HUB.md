# Hub — every setting explained

Page title: **Voice Workstation**
This is the two-in-one page. It has **two tabs**, pick them at the top.

| Tab | Engine | Trained model needed? |
|-----|--------|----------------------|
| **StreamVoiceAnon** | SVA | No — just a voice sample |
| **Applio (RVC)** | RVC | Yes — you must train a model first |

---

## TAB 1 — StreamVoiceAnon

Convert without any training. Give it a sample of the target voice.

### Inputs

| Setting | What you put in | What it means |
|---------|----------------|---------------|
| **Source audio (your voice)** | An audio file, or record with the mic | The speech you want converted. This is the *content* — the words stay the same. |
| **Reference audio(s) — target voice** | One or more audio files | The *voice you want to become*. This is the *timbre/character*. Aim for at least 5–15 seconds of clean speech. More references = steadier result. |

### Settings

| Setting | Type | Default | What it does |
|---------|------|---------|--------------|
| **Alpha (1.0 = keep voice, lower = more anonymization)** | Slider | `1.0` | How much of the *original speaker's voice* is kept. `1.0` = keep the source speaker's characteristics as much as possible (least change to identity, most natural). **Lower values (e.g. `0.5`, `0.2`) push the output further away from the source speaker, so it becomes more anonymized.** If the output still sounds like you, lower it. |
| **Simulate streaming** | Checkbox | Off | Processes audio in chunks as if it were live audio. Same result, different internal path. Only useful when testing how the voice behaves under streaming — leave off for normal file conversion. |
| **Ref crop lengths (seconds, optional)** | Text | empty | Trims each reference file to the first N seconds before use. Enter a single number to cut all references to that length, or several numbers separated by spaces to cut each one differently (e.g. `10 15 8`). Use this to skip noisy intro/silence or trim long references to speed things up. Leave empty to use the whole file. |
| **Pipeline config (VC)** | Dropdown | `configs/config_firefly_arvcasr_8192_delay0_8.yaml` | The model blueprint. **Leave at the default** unless you have a reason to change it. The other option (`hydra_arcs/vc/...`) is an alternate architecture — only for advanced experiments. |
| **Checkpoint — dual_ar_* = conversion model** | Dropdown | `pretrained_checkpoints/dual_ar_delay_0_8.pth` | Which trained AI weights to use. **Leave at the default.** The four choices are parts of the same system (`dual_ar` = the converter, `firefly-gan` = vocoder, `spark_speaker_encoder` = voice encoder, `asr_s2s` = speech recognizer). Picking the wrong one breaks the run. |

> **Which formats can I upload?** MP3, WAV, M4A, FLAC, OGG, OPUS, AAC, AIFF,
> WMA, WebM and MP4 audio all work here — you rarely need to convert anything
> first. Details in `08-MODELS-AND-FILES.md`.

### Outputs

| Output | What it is |
|--------|------------|
| **Output** | The converted audio. Play it, then use the download button in the corner of the player. |
| **Status** | Progress and errors in plain text. If it stops, the reason is written here. |

### How to run it

1. Put your source audio in **Source audio**.
2. Put target voice sample(s) in **Reference audio(s)**.
3. Leave **Alpha = 1.0** and the config/checkpoint at defaults.
4. Press the convert button.
5. Play **Output**.

If the result still sounds like the source speaker, come back and lower **Alpha**.

---

## TAB 2 — Applio (RVC)

Convert using a voice model you trained. Lighter controls than the full Applio
page — the full page has dozens more.

### Inputs

| Setting | Type | What it means |
|---------|------|---------------|
| **Source audio** | Audio | What you want converted. |
| **Voice model** | Dropdown | Which trained model to use. **Empty until you train one.** If it is empty, go to the Applio page → Training tab first, or see **`06-TRAIN-A-MODEL.md`** for the full walkthrough (about 10 minutes of voice gives you a usable model). |
| **Index file path (optional)** | Text | An `.index` file makes the model match the trained voice more precisely. Leave empty to let it pick automatically. Fill it in only if `index_rate` is set above 0 and you have the file. |

### Settings

| Setting | Type | Default | What it does |
|---------|------|---------|--------------|
| **Pitch shift (semitones)** | Slider | — | Moves pitch up/down. `+12` = one octave up, `-12` = down, `0` = no change. Use when the voice sits in the wrong range — e.g. male → female usually needs `+12`. |
| **Index rate** | Slider | `0.75` | How strongly the result is forced to match the trained voice's fine character. `0` = freer/smoother but less accurate; `1` = strictest, can sound artificial. `0.75` is the normal choice. Lower to `0.3–0.5` if the voice sounds warbly. |
| **F0 method** | Dropdown | `rmvpe` | Pitch-detection algorithm. `rmvpe` = recommended default, good balance. `crepe` = slowest, most accurate. `fcpe` = fast, good for music. `hybrid` = mixes methods. |

### Outputs

| Output | What it is |
|--------|------------|
| **Output** | The converted audio. |
| **Status** | Progress / errors. |

### Typical settings by goal

| Goal | Pitch shift | Index rate | F0 |
|------|-------------|-----------|-----|
| Male → female | `+12` | `0.75` | `rmvpe` |
| Female → male | `-12` | `0.75` | `rmvpe` |
| Same-gender voice swap | `0` | `0.75` | `rmvpe` |
| Quality over speed | `0` | `0.8` | `crepe` |

---

## Buttons

The page also has a **load models** action (`/_load_models`) that warms up the
engines. If the first conversion is slow or the model list is empty, use it
once before starting.
