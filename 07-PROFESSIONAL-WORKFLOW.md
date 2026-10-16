# Professional Workflow — the order to do things in

Written for paid/production use: voiceovers, explainer videos, narration,
character work, localization (English ↔ Hindi).

**The single most useful idea in this file:** there are **four stages**, and
doing them **in the wrong order is the #1 cause of bad results**.

```
1. PREPARE  →  2. TRAIN  →  3. CONVERT  →  4. ENHANCE  →  5. DELIVER
   clean the      make the    swap the     fix the      export the
   source first   model       voice        tone         final file
```

Skipping stage 1 makes everything after it worse. Doing stage 4 inside stage 3
(by stacking effects while converting) is the second most common mistake.

---

## Stage 0 — Decide which engine

| Decision | Use |
|----------|-----|
| Must match one specific person's voice, best quality, you have audio of them | **Applio (RVC)** + train a model |
| Need it in 5 minutes, have a short sample | **SVA** (no training) |
| Translate + re-voice English ↔ Hindi | **Dubbing** (the 5th link) |
| Voiceover has a music bed | **Music remover** first |
| Text → narration in a trained voice | **Applio → TTS** |

For professional delivery where quality is judged by a client: **use Applio with
a trained model.** SVA is for situations where there is no time to train.

---

## Stage 1 — PREPARE the source audio

**Never convert noisy audio.** Anything wrong with the source gets baked into
the output and becomes much harder to fix afterwards.

### Your recording should be

| Item | Target |
|------|--------|
| Format | WAV (44.1 kHz or 48 kHz) |
| Channels | Mono (one voice) |
| Level | peaks around −6 dB to −3 dB, no clipping |
| Background | no music, no room echo, no other voices |
| Consistency | same mic, same distance, same room for every take |

### If the source has background music

Use **Music remover** (`04-MUSIC-REMOVER.md`):

| Your situation | Model | Speed |
|----------------|-------|-------|
| Draft / first listen / long file | `FAST - MDX23C` | `Fast` |
| **Standard professional pass** | `FAST - Kim FT` | `Balanced` |
| Audible voice left in the music track | `FAST - Kim FT2 bleedless` | `Balanced` |
| Final export, quality critical | `QUALITY (SLOW) - the original default` | `Quality` |
| Still a little hiss afterwards | re-run with `Post-process - denoise only` | `Quality` |

**Then listen to the clean vocals before going further.** If the voice is still
muddy, fix it here — do not try to fix it after conversion.

### Keeping your masters

Tick **"Also keep the music/instrumental stem"** and download the zip of stems.
You will want the original mix back if a client asks for a revision.

---

## Stage 2 — TRAIN the model (Applio only)

Full walkthrough in **`06-TRAIN-A-MODEL.md`**. The professional-relevant points:

### ⭐ Set the sample rate to 48000 if you deliver video

Training tab → **Model Settings → Sampling Rate**. This is fixed at training
time — you cannot change it later.

| Delivery | Sampling Rate |
|----------|---------------|
| **Video (film, YouTube, ads, narration)** | **`48000`** |
| Music-only / podcast audio | `44100` |
| Don't care / smallest files | `40000` |

This one dropdown decides whether your output drops straight into an NLE
(Premiere, DaVinci, Final Cut) at the right rate, or needs a resample.

### Training data quality beats quantity

- 10 minutes minimum; **30–60 minutes for professional work**.
- Read a variety of sentences (questions, exclamations, soft and loud) — the
  model can only learn the sounds you gave it.
- Tick **Pretrained = ON** (essential with limited data).
- **Save Every Epoch = 5**, **Total Epoch = 50** to start, watch TensorBoard,
  train longer if the loss is still falling.

### Then download the `.pth` + `.index`

Non-negotiable — the session wipes it otherwise.

---

## Stage 3 — CONVERT the voice

### Which page

| Situation | Use |
|-----------|-----|
| One file, quick | **Hub → Applio (RVC)** tab |
| One file, full control | **Applio → Inference → Single** |
| Many files (an episode, a whole course) | **Applio → Inference → Batch** |
| Text to narration | **Applio → TTS** |

### Batch is the professional move

**Inference → Batch**: set **Input Folder** and **Output Folder** and convert a
whole episode at once. Set your preferred settings once and they apply to every
file — much more consistent than re-running single files with slightly different
sliders.

### The three settings that decide quality

| Setting | Start here | What to change it for |
|---------|-----------|----------------------|
| **Pitch extraction algorithm** | `rmvpe` | `crepe` if the audio is hard and you have time; `fcpe` for musical content |
| **Search Feature Ratio** | default | Raise for a stricter match to the trained voice; lower if the output sounds muffled |
| **Index rate** | `0.75` | Raise toward `1` for a tighter voice match; drop to `0.3–0.5` if the voice warbles |
| **Protect Voiceless Consonants** | default | Raise if s/f/t sounds are being eaten |
| **Pitch shift** | `0` | Only if the target voice sits in the wrong range — check with **Proposed Pitch** first |
| **Formant Shifting** | off | To make the voice feel larger/smaller without changing pitch (`m2f` / `f2m` presets) |

**Tip:** tick **Split Audio** for files over a few minutes — it improves
consistency and reduces memory problems on long files.

---

## Stage 4 — ENHANCE the tone

Do this **as a separate pass after conversion**, using **Post-Process** in
Inference, or in your usual audio editor. Keep it subtle — for speech the goal
is intelligibility and evenness, not effect.

Order inside Applio's **Post-Process** chain:

| # | Effect | Sliders | Use for |
|---|--------|---------|---------|
| 1 | **Compressor** | Threshold dB, Ratio, Attack ms, Release ms | Evening out loud/quiet speech. The single most useful effect for narration. |
| 2 | **Limiter** | Threshold dB, Release Time | Safety ceiling so the final file never clips |
| 3 | **Gain** | Gain dB | Final level adjustment |
| 4 | **Clean Audio / Clean Strength** | strength | Removing residual noise — use gently, heavy cleaning sounds underwater |
| 5 | **Reverb** | Room Size, Damping, Wet Gain, Dry Gain, Width | Only if the scene calls for it — keep Wet Gain low |
| 6 | **Chorus / Distortion / Bitcrush / Clipping / Delay** | various | Creative effects, off for professional narration |

**A safe professional starting point:** Compressor on with a moderate ratio,
Limiter on to catch peaks, Gain to bring the level up, everything else off.

### Save your settings as a preset

Inference → **Preset Settings → Preset Name** → save. Then reuse the same
preset for every file in the series, and import it in future sessions via
**Select file to import**. This is what keeps a series sounding consistent.

---

## Stage 5 — DELIVER

### Formats

| Use | Format |
|------|--------|
| Master / archive, anything you may re-edit | **WAV** (lossless) |
| Client delivery under a size limit | `MP3` |
| Lossless but smaller than WAV | `FLAC` |
| Web/social delivery | `MP3` or `M4A` |

Set it in **Export Format** (Inference/TTS/Batch) or in the music remover's
**Output format**.

### What you hand over vs. keep

| Keep locally | Deliver |
|-------------|---------|
| Original recordings | Final converted file |
| Cleaned stems (music remover zip) | A second format if asked |
| The trained `.pth` + `.index` | — |

### ⚠️ The public URL is not your delivery method

The `gradio.live` links are a **remote control surface**, not storage. They die
when the session ends. Always **download the output file** — that is the
deliverable.

---

## Quality control — run this before you deliver

| Check | How | If it fails |
|-------|-----|-------------|
| Words correct, none cut off | Listen all the way through | Raise **Protect Voiceless Consonants**; enable **Split Audio** |
| Voice is actually the target voice | Compare against a known-good sample | Raise **Index rate**; retrain with more data |
| No music or noise audible | Listen on headphones | Re-run music remover with a slower model |
| No warble or robotic artefacts | Listen to sustained vowels | Lower **Index rate**; lower **Search Feature Ratio** |
| Level consistent throughout | Watch the waveform | Compressor on, then Limiter |
| No clipping / distortion on loud parts | Look for flat-topped waveform | Limiter on, lower **Gain dB** |
| Right pitch for the character | Compare with reference | **Pitch shift** (check **Proposed Pitch**) |
| Right sample rate for the project | Check file properties | Train at `48000` for video |
| File plays in your editor/NLE | Import it | Convert to WAV |

---

## Time budget (plan your session)

| Task | Rough time |
|------|-----------|
| Workstation start-up | ~15 min |
| Music removal (1 min of audio) | 1–3 min |
| Preparing + preprocessing training data | 5–10 min |
| Feature extraction (10 min data) | 5–10 min |
| Training (10 min data) | 10–30 min |
| Training (30–60 min data) | 30 min – couple of hours |
| Converting (1 min of audio) | ~1 min |
| Batch of 10 files | ~10–15 min |
| Model re-upload next session | ~1 min |

**Practical advice:** do training in one session and keep that session alive
for the conversions in the same sitting — re-uploading a model each time is
quick, but it is still friction.

---

## Failure modes ranked by how often they happen

| Symptom | Most likely cause | Fix |
|---------|-------------------|-----|
| Output still sounds like the source voice | Not enough model training, or index rate too low | Train longer / more data; raise **Index rate** |
| Voice warbles or "warble-robotic" | Index rate / search feature too strict | Lower **Index rate** to `0.3–0.5`; lower **Search Feature Ratio** |
| Words eaten or mushy | Consonants unprotected, or over-cleaning | Raise **Protect Voiceless Consonants**; reduce **Clean Strength** |
| Music audible in the result | Music removal too fast a model | Re-run with `Quality` preset |
| Long file degrades halfway | Memory / context limit | Enable **Split Audio** |
| Voice sounds wrong-pitched | Pitch not adjusted | Tick **Proposed Pitch**, or set **Pitch shift** manually |
| My model is gone | Session ended before download | Download `.pth` + `.index` — see `06-TRAIN-A-MODEL.md` |
| Page won't open / 404 | Kaggle session ended | The `gradio.live` links are tied to the live session |

---

## The short version (pin this)

1. **Clean the source first** — music remover, and make sure it's genuinely clean.
2. **Train at 48000** if you deliver video. Download the `.pth` + `.index`.
3. **Convert** with `rmvpe`, Index rate `0.75`, **Split Audio** on for long files.
4. **Enhance separately** — Compressor, Limiter, Gain. Save it as a preset.
5. **Export WAV**, download it, run the checklist, then deliver.
