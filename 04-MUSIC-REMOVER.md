# Music Remover — every setting and model explained

Strips background music/instrumentals off a voiceover so that only the clean
speaking voice is left. Run this **before** converting the voice.

API it exposes: `/separate_audio`

> **Which formats?** WAV, FLAC, MP3, OGG, M4A, AAC, OPUS and WMA are all
> accepted — MP3 included. Output is WAV, MP3 or FLAC (your choice).
> Full format and file guide: `08-MODELS-AND-FILES.md`.

---

## Inputs

| Setting | What you put in |
|---------|----------------|
| **Input audio (voiceover, any length)** | The file with speech + music mixed together. Any length; longer files take proportionally longer. |

---

## Settings

| Setting | Type | Default | What it means |
|---------|------|---------|---------------|
| **Separation model** | Dropdown | `mel_band_roformer_kim_ft_unwa.ckpt` (`FAST - Kim FT`) | Which AI model does the splitting. See the full table below. |
| **Speed / quality** | Radio | `Balanced` | How much compute to spend. `Fast` = quickest, slightly rougher. `Balanced` = the sensible default. `Quality` = slowest, cleanest cut. |
| **Output format** | Radio | `WAV` | File type of the result: `WAV` (lossless, biggest), `MP3` (small), `FLAC` (lossless, compressed). |
| **Also keep the music/instrumental stem** | Checkbox | Off | When **on**, you get *both* files: the clean vocals **and** the leftover music. When off, you only get the vocals (faster). |
| **Status** | Text | — | Progress and errors. |

---

## Outputs

| Output | What it is |
|--------|------------|
| **Clean vocals (feed this to Applio)** | The speech-only track. **This is the file you take to Hub/Applio/SVA.** |
| **Other stems / zip of everything** | Every separated part, or a zip of all of them — only filled in when **Also keep the music/instrumental stem** is on. |
| **What was produced** | A plain-text list of the files it created and where they are. |

---

## The models — full list, in plain words

Models grouped by speed tier, exactly as they appear in the dropdown.

### FAST tier

| Model name (as shown) | Actually good at |
|-----------------------|------------------|
| **FAST - Kim FT. Best speed/quality balance. Default choice.** | The all-round default. Good quality, decent speed. Start here. |
| **FAST - Kim FT2. Slightly cleaner, slightly slower.** | A touch cleaner than Kim FT if you have a little more time. |
| **FAST - Kim FT2 bleedless. Best when the singer 'leaks' into the music.** | Use when you can hear bits of the voice *in* the music track afterward. |
| **FAST - becruily vocals.** | Alternative vocal model — try if the Kim models leave artefacts. |
| **FAST - Gabox vocals.** | Another alternative vocal model. |
| **FAST - generic MelBand vocals.** | Generic model, generally reliable, slightly less sharp than Kim FT. |
| **FAST - MDX23C. Very fast, good enough for voice cleanup.** | The quickest. Use for long files or a first listen; switch to a slower model for the final export. |

### BALANCED tier

| Model name (as shown) | Actually good at |
|-----------------------|------------------|
| **BALANCED - SYHFT V2.5.** | Good quality without the slow tier's wait. |
| **BALANCED - SYHFT V3.** | Newer Syhft version. |
| **BALANCED - instrumental v2.** | Optimised to leave a *clean music* stem behind — use when you want the music, not the voice. |
| **BALANCED - instrumental.** | Same idea, previous version. |

### QUALITY (SLOW) tier

| Model name (as shown) | Actually good at |
|-----------------------|------------------|
| **QUALITY (SLOW) - the original default. Best quality, ~2.5x realtime.** | The best cut of all, but slow: roughly 2.5 minutes of processing per minute of audio. Use for the final render. |
| **QUALITY (SLOW) - BS-Roformer ep_368.** | The strongest single model. Slowest of all. |

### Post-process tier (repair, not first-pass)

These are applied **after** a normal separation to clean up leftovers. Do not
use them as the only step.

| Model name (as shown) | What it does |
|-----------------------|--------------|
| **Post-process - kills vocal bleed leaking from the music.** | Removes voice that bled into the music stem. |
| **Post-process - denoise + debleed.** | Noise removal **and** vocal bleed removal. |
| **Post-process - denoise only (hiss/fan hum, not music).** | Removes hiss/fan/room noise. Does **not** remove music. |

### Other model (from the library catalogue)

Six entries named **"Other model (from the library catalogue)"**. Use these to
pick a model from the tool's own model library that is not pre-loaded in the
list. Advanced — you normally never touch these.

---

## How to actually use it

1. Drop your mixed file into **Input audio**.
2. Leave **Separation model** at the default and **Speed / quality** at `Balanced`.
3. Tick **Also keep the music/instrumental stem** if you want the music too.
4. Run it.
5. Download **Clean vocals**.
6. Take that file to **Hub** (StreamVoiceAnon tab), **SVA**, or **Applio** and
   convert it there.

## Picking settings by situation

| Situation | Model | Speed |
|-----------|-------|-------|
| First try / long file | `FAST - MDX23C` | `Fast` |
| Normal voiceover cleanup | `FAST - Kim FT` | `Balanced` |
| You can hear voice in the music afterwards | `FAST - Kim FT2 bleedless` | `Balanced` |
| Music has a strong beat you want to keep | `BALANCED - instrumental v2` | `Balanced` |
| Final export, quality matters most | `QUALITY (SLOW) - the original default` | `Quality` |
| Output still slightly noisy | run once normally, then again with `denoise only` | `Quality` |

## Timing expectations

| Speed setting | Rough processing time |
|---------------|----------------------|
| `Fast` | close to real-time |
| `Balanced` | a bit slower than real-time |
| `Quality` | ~2.5× real-time or worse |

The **first** run is slower still, because the chosen model downloads first.
