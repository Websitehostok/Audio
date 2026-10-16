# Models, File Formats, and "which file is what?"

Answers three questions:

1. **Can I use MP3 (or any other format)?** — yes, see below
2. **What is every model, and which tool wants which?** — the master list
3. **There are hundreds of files — which one has my audio in it?** — the file map

---

# Part 1 — What audio formats you can use

### Applio (Inference, Batch, TTS, Realtime)

Accepts (verified in the source):

```
wav  mp3  flac  ogg  opus  m4a  mp4  aac  alac  wma  aiff  webm
```

**Yes, MP3 works.** So does M4A, FLAC, OGG, OPUS, AAC, AIFF, WMA, WebM and even
MP4 audio.

**Output is always WAV** (`_output.wav`), regardless of what you fed in, unless
you change **Export Format**.

### Music remover

Accepts:

```
wav  flac  mp3  ogg  m4a  aac  opus  wma
```

**MP3 works.** Output is whatever you pick in **Output format** (WAV/MP3/FLAC),
default **WAV**.

### Hub → StreamVoiceAnon tab / SVA page

Accepts standard browser audio uploads (WAV, MP3, FLAC, OGG, M4A and the rest).

### So what should you actually upload?

| Situation | Upload |
|-----------|--------|
| Best possible quality | **WAV** |
| Client sent you MP3 | **MP3 is fine** — just use it |
| File from a phone / voice memo | **M4A** — works directly, no conversion needed |
| Video you recorded | **MP4** works in Applio; drop the audio into Music remover or Hub if it is large |
| Podcast / interview | MP3 or WAV both fine |

**You almost never need to convert your file first.** MP3 is fully supported.

One caveat: **you get out roughly what you put in**. If the input MP3 is
low-bitrate (64–96 kbps), the result will sound as limited as the source — that
is the input's fault, not the tool's. 192 kbps+ MP3 or any WAV is ideal.

---

# Part 2 — Every model, and which tool uses it

There are **five different model systems** in this workstation. They are not
interchangeable — each tool looks for its own kind.

---

## A. Music remover models (separation models)

You pick these in the **Separation model** dropdown. They split "voice" from
"everything else".

**Full explanations of every option are in `04-MUSIC-REMOVER.md`.** Quick map:

| Tier | Models | When |
|------|--------|------|
| FAST | `Kim FT`, `Kim FT2`, `Kim FT2 bleedless`, `becruily`, `Gabox`, `generic MelBand`, `MDX23C` | Everyday work. Kim FT is the default. |
| BALANCED | `SYHFT V2.5`, `SYHFT V3`, `instrumental v2`, `instrumental` | When you want the *music* kept clean |
| QUALITY (SLOW) | `the original default`, `BS-Roformer ep_368` | Final professional render |
| Post-process | `kills vocal bleed`, `denoise + debleed`, `denoise only` | Applied *after* a normal pass, to repair |
| Other | 6 × `Other model (from the library catalogue)` | Picking from the tool's own library |

---

## B. SVA "checkpoints" + config (conversion models)

You pick these on the **SVA page** and in the **Hub → StreamVoiceAnon tab**.
These are **one model split into four files** — not four alternatives.

| Dropdown option | The file | What it actually is |
|-----------------|----------|---------------------|
| `dual_ar_delay_0_8.pth` | the converter | **This is the one you want.** The actual voice-conversion model. |
| `asr_s2s_bsq_8192_causal_down_whisper.pth` | the recogniser | Internal speech-recognition part. Not a standalone converter. |
| `firefly-gan-vq-fsq-8x1024-21hz-generator.pth` | the vocoder | Rebuilds the waveform. Supporting part. |
| `spark_speaker_encoder.pth` | the speaker encoder | Turns voices into fingerprints. Supporting part. |

**Leave this at `dual_ar_delay_0_8.pth`.** Choosing a different one is the
classic beginner mistake — people see four checkpoints and assume they are four
quality levels. They are four parts of one machine.

**Pipeline config (VC) dropdown** — `config_firefly_arvcasr_8192_delay0_8.yaml`
is the blueprint that goes with the checkpoint. Leave at the default
(`.../hydra_arcs/vc/...` is an alternate architecture for experiments).

---

## C. Applio embedder models

Radio button, appears in Inference, Training and TTS.

| Option | What it is | When to use |
|--------|-----------|-------------|
| `contentvec` | Default | **Always start here.** |
| `spin` | Alternative | If contentvec gives artefacts |
| `spin-v2` | Newer variant | Sometimes better for certain voices |
| `chinese-hubert-base` | Language-specific | Chinese-language training data |
| `japanese-hubert-base` | Language-specific | Japanese-language training data |
| `korean-hubert-base` | Language-specific | Korean-language training data |
| `custom` | Your own upload | Advanced — via the Custom Embedder accordion |

The embedder must be **the same one you trained with**, otherwise the model will
not load properly. If you trained with `contentvec`, convert with `contentvec`.

---

## D. Applio pretrained / base models

**Training tab → Architecture** (`RVC` / `Applio`), **Vocoder**
(`HiFi-GAN` / `RefineGAN`), and the **Pretrained** toggle.

| Item | What it is |
|------|-----------|
| **Pretrained = ON** | Start training from a model that already understands speech. **Essential** for small datasets. |
| **Architecture** | `RVC` is the safe default. |
| **Sampling Rate** | `32000` / `40000` / `48000`. **Use `48000` for video.** Fixed at training time — you cannot change it later. |
| **Vocoder** | `HiFi-GAN` default; `RefineGAN` is the alternative. |
| Custom Pretrained G / D | Your own generator/discriminator files (advanced). |
| **Index Algorithm** | `Auto` / `Faiss` / `KMeans` — how the search index is built. `Auto` is fine. |

**Download tab → Pretrained dropdown**: ready-made well-known models
(`Beatz Forge`, `DMR V1`, `Italia`, `IMA V1`, `KLM4`, `Nanashi v1.7`,
`Ov2Super`) — useful starting points if you don't want to train from scratch.

---

## E. Your own trained model

The `.pth` + `.index` pair you create (see `06-TRAIN-A-MODEL.md`). This is the
one that appears as `myvoice` (or whatever you named it) in every model
dropdown across the workstation.

**Everything above is a base model. This is your model.** They do not mix —
you cannot use a music-remover model for conversion, or an SVA checkpoint in
Applio.

---

# Part 3 — "There are too many files, which one has my audio?"

## The extension tells you what it is

| Ends in | It is | Where from |
|---------|------|-----------|
| `.wav` | **Finished audio.** This is what you download. | Applio output |
| `.mp3` / `.flac` / `.ogg` / `.m4a` | Audio, usually an **input** you uploaded (or an output if you changed Export Format) | your uploads |
| `_output.wav` | **A converted file.** The `_output` suffix is the marker. | Applio Inference |
| `vocals` (no extension) / `Vocals` in filename | **Clean speech from the music remover** | Music remover |
| zip of stems | The separated parts | Music remover (with *keep both* on) |
| `.pth` | **A trained voice model.** Your work — never delete. | Training |
| `.index` | The model's accent/timbre index. Pairs with the `.pth`. | Training |
| `.ckpt` | A separation/voice model file (base models) | ships with the workstation |
| `.bin` | An embedder or encoder model file | ships / custom upload |
| `.json` | Config, preset, or index settings | everywhere |
| `.yaml` | Model blueprint (the SVA config) | ships with SVA |
| `.zip` | A bundle — either a plugin, a dataset, or stems | everywhere |
| `.npy` | Raw pitch/feature data — not playable audio | internal |
| `.txt` | A log or text-to-speech input | logs / TTS |

---

## Where to find your file

| I want | Look here |
|--------|-----------|
| The audio I just converted | The **Output** / **Export Audio** player on the page — download from there |
| Files written to disk | Applio saves to `assets/audios/` — names end in `_output.wav` |
| A specific file the log mentions | The log box names it; music remover says it in **"What was produced"** |
| All separated stems | The **Other stems / zip of everything** file on the music remover |

---

## The trick: use the labels, not the folders

You never need to browse the Kaggle filesystem. Every tool tells you exactly
what it made:

| Page | Where the answer appears |
|------|--------------------------|
| Applio Inference | **Export Audio** player, and **Select Audio** dropdown lists every saved file |
| Applio Batch | **Batch conversion output** log |
| Applio TTS | **Export Audio** player |
| Music remover | **"What was produced"** lists every file by name |
| SVA / Hub | **Output** player + **Status** box |

**Applio's "Select Audio" dropdown is the fastest way to see what audio files
exist**, and **"Clear Outputs (Deletes all audios in assets/audios)"** removes
the old ones.

---

## The two files you must never lose

```
myvoice.pth      ← the trained voice model
myvoice.index    ← its matching accent/timbre index
```

These were made by you, they are not shipped, and **they are erased when the
session ends.** Download both after every training run. See
`06-TRAIN-A-MODEL.md`.

---

## Quick sanity check before you deliver

| Question | Check |
|----------|-------|
| Is this the converted file or my original? | Converted files end in `_output.wav` |
| Is this the clean vocals or the music? | Vocals = the clean speech; the music stem is the other one |
| Did I get both stems? | Only if **"Also keep the music/instrumental stem"** was ticked |
| Is it the format I promised the client? | Use **Export Format** before downloading |
| Did I download the model files? | `.pth` + `.index` both on your PC |
