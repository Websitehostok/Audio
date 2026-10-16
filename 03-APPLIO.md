# Applio — every tab and setting explained

This is the full professional page. It has **24 tabs** and hundreds of controls.
This file explains each tab and what it is for.

**Two things to note before anything else:**

1. **There is no voice model until you train one.** The Inference tab's
   *Voice Model* dropdown will be empty. That is normal — either train a model
   (Training tab) or use the **SVA** page, which needs no training.
2. **Several tabs ask you to tick "I agree to the terms of use"** before they
   run. Nothing works until you do.

---

## The tab map

| Tab | What it is for |
|-----|----------------|
| **Inference** | Convert audio with a trained model (Single + Batch) |
| **Training** | Train a new voice model from audio |
| **TTS** | Text → speech (typed text or a .txt file), optionally re-voiced |
| **Voice Blender** | Mix two trained models into one |
| **Realtime** | Live voice changing (needs a sound device) |
| **Plugins** | Install a plugin from a .zip |
| **Download** | Download pretrained models from a link |
| **Report a Bug** | Pack up logs for a bug report |
| **Extra** | Model info, F0 curve export, Audio analyzer |
| **Settings** | Appearance, audio device, training defaults |
| **TensorBoard** | Show the training graph |

---

## 1. Inference

Two sub-tabs: **Single** (one file) and **Batch** (a whole folder). Both have the
same settings — only the input differs (a file vs. input/output folders).

### Model selection (top of tab)

| Setting | What it means |
|---------|---------------|
| **Voice Model** | Which trained model to convert with. Empty until you train one. |
| **Filter** | Text to narrow the Voice Model list when you have many. |
| **Index File** | The `.index` sidecar that sharpens accent/timbre matching. Leave on *Auto/empty* if unsure. |

### Input

| Setting | What it means |
|---------|---------------|
| **Upload Audio** | The audio to convert. |
| **Select Audio** | Or pick a file already on the Kaggle disk. |
| **Input Folder / Output Folder** | *Batch only* — convert every file in a folder at once. |

### Advanced Settings accordion

| Setting | Type | What it means |
|---------|------|---------------|
| **Output Path** | Text | Where to write results. Leave empty for the default. |
| **Export Format** | Radio | `WAV`/`MP3`/`FLAC`/`OGG`/`M4A`. `WAV` = lossless biggest, `MP3` = smallest. |
| **Speaker ID** | Dropdown | For multi-speaker models — which speaker to use. `0` unless your model has more. |
| **Split Audio** | Checkbox | Cuts the input into pieces, converts each, rejoins. Helps long files. |
| **Autotune** | Checkbox | Snaps pitch to a musical scale. Off unless you want a singing/auto-tuned effect. |
| **Autotune Strength** | Slider | How aggressive autotune is. |
| **Proposed Pitch** | Checkbox | Auto-suggests the best pitch shift for the file. Use this if you don't know what shift to pick. |
| **Proposed Pitch Threshold** | Slider | Cut-off for that suggestion. |
| **Clean Audio** | Checkbox | Light noise cleanup before conversion. |
| **Clean Strength** | Slider | How much cleanup. |
| **Formant Shifting** | Checkbox | Changes voice *character* without changing pitch — this is the male/female "size" of the voice, separate from pitch. |
| **Post-Process** | Checkbox | Applies the effects chain below. |
| **Browse presets for formanting** | Dropdown | `random` / `m2f` (male→female) / `f2m` (female→male) — ready-made formant settings. |
| **Quefrency for formant shifting** | Slider | Fine control of the formant shift. |
| **Timbre for formant shifting** | Slider | Fine control of tone colour. |
| **Reverb** + 6 sliders | Checkbox | Adds room reverb: **Room Size, Damping, Wet Gain, Dry Gain, Width, Freeze Mode**. |
| **Pitch Shift** + **Pitch Shift Semitones** | Checkbox | Manual pitch change in semitones (`+12`/`-12` = one octave). Must be ticked to take effect. |
| **Limiter** + Threshold dB / Release Time | Checkbox | Prevents clipping/loudness spikes. |
| **Gain** + Gain dB | Checkbox | Overall volume change in decibels. |
| **Distortion** + Distortion Gain | Checkbox | Adds edge/grit. |
| **Chorus** + 5 sliders | Checkbox | Thickens the voice. Controls: **Rate Hz, Depth, Center Delay ms, Feedback, Mix**. |
| **Bitcrush** + Bitcrush Bit Depth | Checkbox | Lo-fi / retro digital sound. |
| **Clipping** + Clipping Threshold | Checkbox | Hard cuts the waveform for a rough sound. |
| **Compressor** + Threshold dB / Ratio / Attack ms / Release ms | Checkbox | Evens out loudness. |
| **Delay** + Seconds / Feedback / Mix | Checkbox | Echo. |

### Preset Settings accordion

| Setting | What it means |
|---------|---------------|
| **Select Custom Preset** | `Default`, `Music`, `Good for Anything` — starting points. |
| **Select file to import** | Load a saved preset from disk. |
| **Preset Name** | Name to save the current settings under. |
| **Pitch** | Base pitch setting inside the preset. |
| **Search Feature Ratio** | How much the encoder searches for matching features — higher = stricter match to training. |
| **Volume Envelope** | How much of the original loudness shape is kept. |
| **Protect Voiceless Consonants** | Stops S/F/T sounds from being smeared. Raise if speech is mushy. |
| **Pitch extraction algorithm** | `crepe`, `crepe-tiny`, `rmvpe`, `fcpe`. **`rmvpe` is the default recommendation.** |
| **Embedder Model** | The voice-feature model: `contentvec` (default), `spin`, `spin-v2`, language-specific hubert variants, or `custom`. |

### Custom Embedder accordion

Upload your own embedder: **Select Custom Embedder**, **Folder Name**,
**Upload .bin**, **Upload .json**. Advanced — skip unless you know you need it.

### Outputs

| Output | What it is |
|--------|------------|
| **Conversion output** | Log of what happened. |
| **Export Audio** | The finished file. |

---

## 2. Training — making a new voice model

> **Full step-by-step walkthrough in `06-TRAIN-A-MODEL.md`** — it covers
> recording ~10 minutes of voice, the exact settings, how long it takes, and
> how to keep the model so you can reuse it in every future session.
> This section is the reference for what each control does.

Training turns a pile of someone's speech into a `.pth` model you can convert with.

### Model Settings

| Setting | Options | Meaning |
|---------|---------|---------|
| **Model Name** | text | Name of the model you are creating. |
| **Architecture** | `RVC` / `Applio` | Underlying architecture. `RVC` is the safe default. |
| **Sampling Rate** | `32000`/`40000`/`48000` | Model sample rate. `40000` is the common default. |
| **Vocoder** | `HiFi-GAN` / `RefineGAN` | The part that rebuilds the waveform. `HiFi-GAN` is default. |

### Advanced Settings

| Setting | Meaning |
|---------|---------|
| **CPU Cores** | CPU threads used for preparing data. |
| **GPU Number** | Which GPU to train on. |
| **GPU Information** | Shows detected GPUs. |

### Preprocess

| Setting | Meaning |
|---------|---------|
| **Dataset Path** | Folder of the training audio. |
| **Dataset Creator** | Use the built-in dataset builder below. |

### Dataset Creator

| Setting | Options | Meaning |
|---------|---------|---------|
| **Dataset Name** | text | Name of the dataset to build. |
| **Upload Audio Dataset** | file | Upload a zip of training audio. |
| **Audio cutting** | `Skip`/`Simple`/`Automatic` | How to split long recordings. `Automatic` finds silences. |
| **Chunk length (sec)** | slider | Size of each training slice in seconds. |
| **Overlap length (sec)** | slider | Overlap between slices so no word is cut in half. |
| **Noise filter** | checkbox | Isolate voice from noise while preparing. |
| **Normalization mode** | `none`/`pre`/`post` | When to even out loudness. |
| **Noise Reduction** | checkbox | Remove noise. |
| **Noise Reduction Strength** | slider | How hard. |
| **Preprocess output** | text | Log of this stage. |

### Extract

| Setting | Options | Meaning |
|---------|---------|---------|
| **Pitch extraction algorithm** | `crepe`/`crepe-tiny`/`rmvpe` | How pitch is found in the training data. `rmvpe` recommended. |
| **Embedder Model** | `contentvec`/`spin-v2`/`custom` | Voice feature extractor for training. |
| **Silent training files** | slider | How much silence the trainer tolerates in a file before dropping it. |
| **Custom Embedder** | dropdown + uploads | Use your own. |
| **Feature extraction output** | text | Log of this stage. |

### Training

| Setting | Options | Meaning |
|---------|---------|---------|
| **Batch Size** | slider | Files processed per step. Higher = faster but needs more memory. |
| **Save Every Epoch** | slider | Save a checkpoint every N epochs. |
| **Total Epoch** | slider | How many epochs to train. More = better, up to a point. |
| **Save Only Latest** | checkbox | Keep just the newest checkpoint (saves disk). |
| **Save Every Weights** | checkbox | Save each epoch's full weights (lots of disk). |
| **Pretrained** | checkbox | Start from a pretrained model — **much faster**, recommended. |
| **Fresh Training** | checkbox | Start from zero. Slower, needs more data. |
| **Cache Dataset in GPU** | checkbox | Keep training data on the GPU. Faster if it fits. |
| **Checkpointing** | checkbox | Allows resuming a crashed training. |
| **Shutdown after finishing** | checkbox | Turn off the session when done. |
| **Custom Pretrained** | checkbox | Supply your own starting weights. |
| *(Custom Pretrained on)* **Upload Pretrained Model**, **Custom Pretrained G**, **Custom Pretrained D** | | Your generator/discriminator files. |
| **Index Algorithm** | `Auto`/`Faiss`/`KMeans` | How the search index is built. `Auto` is fine. |
| **I agree to the terms of use** | checkbox | **Must be ticked.** |
| **Training output** | text | Live training log. |

### Export Model

When training finishes, export the model so it appears in Inference. After
exporting, it is available in **every** model dropdown in the workstation —
Hub's Applio tab, Inference (Single/Batch), TTS, Voice Blender and Realtime.

| Setting | Meaning |
|---------|---------|
| **Exported Pth file** | Pick the trained weights to export. |
| **Pth file** | Which `.pth` this is. |
| **Exported Index File** | Pick the index to export. |
| **Index File** | Which `.index` this is. |

> **Then download the `.pth` + `.index`** via the Download tab — otherwise the
> model is lost when the session ends. See `06-TRAIN-A-MODEL.md`.

### Training data requirements (what actually matters)

- **10 minutes minimum** of clean speech; **30–60 minutes** is much better.
- One speaker only, no music, minimal noise.
- Normal speaking voice, consistent recording setup.

---

## 3. TTS — text to speech

Turns text into speech, in a trained voice.

### Top of tab

| Setting | Meaning |
|---------|---------|
| **Voice Model** | The trained model to speak with. |
| **Filter** / **Index File** | Same role as in Inference. |
| **TTS Voices** | The base *text reader* voice (Microsoft neural voices, hundreds of languages). This generates the speech before your model re-voices it. |
| **TTS Speed** | How fast the text is read. |

### Sub-tab: Text to Speech

| Setting | Meaning |
|---------|---------|
| **Text to Synthesize** | Paste your text here. |

### Sub-tab: File to Speech

| Setting | Meaning |
|---------|---------|
| **Upload a .txt file** | Upload text instead of typing. |
| **Input path for text file** | Or point at a file already on disk. |

### Advanced Settings

| Setting | Meaning |
|---------|---------|
| **Output Path for TTS Audio** | Where the raw text-to-speech file goes. |
| **Output Path for RVC Audio** | Where the re-voiced file goes. |
| **Export Format** | `WAV`/`MP3`/`FLAC`/`OGG`/`M4A`. |
| **Speaker ID** | For multi-speaker models. |
| **Split Audio** | Process in chunks (helps long text). |
| **Autotune / Autotune Strength / Proposed Pitch / Threshold** | As in Inference. |
| **Clean Audio / Clean Strength** | Noise cleanup. |
| **Pitch** | Pitch inside the preset. |
| **Search Feature Ratio / Volume Envelope / Protect Voiceless Consonants** | As in Inference. |
| **Pitch extraction algorithm** | `crepe`/`crepe-tiny`/`rmvpe`/`fcpe`. |
| **Embedder Model** | As in Inference. |
| **The f0 curve represents the variations in the bass and treble** | Upload an F0 curve file if you have one (advanced). |
| **I agree to the terms of use** | Must be ticked. |

### Outputs

**TTS output** (log) and **Export Audio** (the file).

---

## 4. Voice Blender

Mixes two trained models into a new one.

| Setting | Meaning |
|---------|---------|
| **Model Name** | Name for the blended result. |
| **Drop your first model here** / **Path to first model** | First source model. |
| **Drop your second model here** / **Path to second model** | Second source model. |
| **Blend Ratio** | `0` = all model A, `1` = all model B, `0.5` = even mix. Drag to taste. |
| **Blend output** | Log. |
| **Download Model** | Save the blended model. |

---

## 5. Realtime — live voice changing

**Needs a working sound device (mic + speakers).** On Kaggle there is no
microphone, so this tab is effectively **unusable in this hosted setup** — it is
listed here so you know why it won't produce sound.

- **Audio Settings** — Input Device, Input Gain (%), Input ASIO Channel, Output
  Device, Output Gain (%), Output ASIO Channel, Stereo toggle, Monitor Device
  (Use Monitor Device, Monitor Device, Monitor Gain %, Monitor ASIO Channel),
  Record Audio (Output Path, Export Format, Export Audio), Exclusive Mode,
  Enable VAD (voice activity detection — only processes when you talk).
- **Model Settings** — the same conversion controls as Inference.
- **Performance Settings** — **Chunk Size (ms)**, **Crossfade Overlap Size (s)**,
  **Extra Conversion Size (s)**, **Silence Threshold (dB)**. These control
  latency vs. smoothness for live use.

---

## 6. Plugins

| Setting | Meaning |
|---------|---------|
| **Drop a plugin.zip here** | Install an add-on. |

---

## 7. Download

| Setting | Options | Meaning |
|---------|---------|---------|
| **Model Link** | text | Paste a download URL for a model. |
| **Download output** | text | Progress. |
| **Drop your .pth and .index files** | file | Upload models you already have. |
| **Pretrained** | `Beatz Forge`, `DMR V1`, `Italia`, `IMA V1`, `KLM4`, `Nanashi v1.7`, `Ov2Super` | Download a well-known pretrained model by name. |
| **Sampling Rate** | `32k`/`40k`/`48k` | Must match your target. |
| **Pretrained G** / **Pretrained D** | text | Manual paths to generator/discriminator. |
| **Custom Pretrained** | checkbox | Use the manual paths above. |

---

## 8. Report a Bug

Creates a support bundle of logs to attach to a bug report. One button.

---

## 9. Extra

### Model information

| Setting | Meaning |
|---------|---------|
| **Path to Model** | Which model to inspect. |
| **Model information output** | Shows what is inside it (epochs, sample rate, speaker count). |

### F0 Curve

| Setting | Options | Meaning |
|---------|---------|---------|
| **Upload Audio** | audio | Audio to analyse. |
| **Pitch extraction algorithm** | `crepe`/`fcpe`/`rmvpe` | Method used. |
| **F0 Curve** | file | The exported pitch-over-time graph. Use it to check a recording's pitch before training or converting. |

### Audio Analyzer

| Setting | Meaning |
|---------|---------|
| **Audio analysis output** | Technical report on the loaded audio. |

---

## 10. Settings

### General

| Setting | Options | Meaning |
|---------|---------|---------|
| **Enable model/index list filter** | checkbox | Adds the Filter box to model lists. |
| **Enable RMVPE high-register correction** | checkbox | Stops high notes being mis-detected with `rmvpe`. Useful for female/child voices. |
| **Correction mode** | `true_pitch`/`fold` | How the correction behaves. |
| **F0 ceiling (Hz)** | slider | The highest pitch the tool will look for. |
| **Enable Applio integration with Discord presence** | checkbox | Cosmetic. |
| **Enable ASIO** | checkbox | Low-latency audio on Windows. |
| **Sample Rate** | `44100`…`192000` | App audio rate. |
| **Theme** | dropdown | Colour scheme. |
| **Version Checker** | text | Current version info. |
| **Language** | dropdown | UI language. |

### Training

| Setting | Options | Meaning |
|---------|---------|---------|
| **Model Author Name** | text | Stored in the model file as credit. |
| **Model author output** | text | Log. |
| **Precision** | `fp32`/`fp16`/`bf16` | Numerical precision of training. `fp32` = safest, `fp16` = faster/less memory but can be unstable on CPU. |
| **Precision output** | text | Log. |

---

## 11. TensorBoard

| Setting | Meaning |
|---------|---------|
| **TensorBoard URL** | Opens the live training graph so you can watch loss/learning progress while training runs. |
