# Glossary — every term in the workstation, in plain words

A–Z. If you only remember one thing: **RVC = you train first; SVA = you don't.**

---

## A

**Alpha** (SVA) — how much of the *original speaker's* voice the tool keeps.
`1.0` = keep as much as possible (most natural, least change to speaking identity).
Lower = pushes the output further from the source speaker, so it is more
anonymized.

**Anonymize** — change the voice enough that listeners cannot identify the
original speaker. Lowering **Alpha** does this.

**Architecture** (Applio Training) — the underlying model design. Choices are
`RVC` and `Applio`. `RVC` is the safe default.

**ASIO** — a low-latency Windows audio driver system. Only relevant for live
mic work, i.e. not usable on Kaggle.

**Autotune** — snaps pitch onto a musical scale, the "robot singing" effect.
Off for normal speech.

## B

**Batch** (Applio) — convert a whole folder of files in one go, instead of one
file at a time.

**Batch Size** — how many audio slices the trainer looks at per step. Higher is
faster but uses more memory.

**Bitcrush** — an effect that makes audio lo-fi/retro digital.

**Bleed** — when the voice leaks into the music track after separation (or the
music leaks into the voice). Some models are built to reduce it.

## C

**Chunk length / Chunk Size** — the size of one piece of audio when a long file
is cut into pieces for processing. Smaller chunks = less memory, more seams.

**Checkpoint** — a saved snapshot of an AI model's weights. In SVA's dropdown it
means *which trained weights file to load*; in training it means *the saved
progress you can resume from*.

**Clipping** — an effect that hard-cuts the waveform, making a rough sound.

**Compressor** — an effect that evens out loudness, so quiet parts come up and
loud parts come down.

**Contentvec** — the default *embedder model*: a neural network that extracts
"what the speaker sounds like" from audio.

**Crepe / Crepe-tiny** — pitch-detection algorithms. `crepe` is the most
accurate but slowest; `crepe-tiny` is the fast, less accurate version.

**Crossfade Overlap Size** — how much neighbouring chunks are blended together
to hide the seams between them.

## D

**Dataset** — the collection of audio files you train a model on.

**Discriminator (D)** — the half of the training system that learns to tell
real from fake audio. Advanced only.

**Distortion** — an effect that adds grit/edge.

**Dry Gain** — the amount of *original*, untreated sound in the mix. Opposite of
wet.

## E

**Epoch** — one full pass through the training data. More epochs generally means
a better model, up to the point where it stops improving.

**Embedder Model** — the network that turns the speaker's voice into a
mathematical "voice fingerprint". Options include `contentvec`, `spin`,
`spin-v2`, and language-specific hubert variants.

**Exclusive Mode** — lets one app take full control of a sound device. Windows
only, irrelevant here.

**Export Format** — the file type produced: `WAV`, `MP3`, `FLAC`, `OGG`, `M4A`.

## F

**F0** — the fundamental pitch of a voice, in Hz. "F0 method" = "how do we find
the pitch".

**F0 method / Pitch extraction algorithm** — the algorithm used to detect pitch.
`rmvpe` is the recommended default (fast and accurate). `crepe` is slowest but
most accurate. `fcpe` is fast and good with music. `crepe-tiny` is quick and
rough.

**F0 Curve** — a graph of pitch over time, exported to inspect a recording's
pitch before training/converting.

**Formant Shifting** — changes the *size* and character of the voice
(male/female feel) **without changing pitch**. This is the control to use when
you want the voice to feel bigger or smaller but stay on the same note.

**Fresh Training** — start a model from zero instead of from a pretrained base.

## G

**Generator (G)** — the half of the training system that actually produces the
fake/converted audio. Advanced only.

**Gain** — overall volume. **Gain dB** = how much louder (+) or quieter (-).

## H

**Hub** — the two-in-one page with the StreamVoiceAnon tab and the Applio tab.
The quickest way to convert.

## I

**Index / Index file** — a `.index` sidecar file built during training that lets
the model match the trained voice's fine details more precisely. Empty index =
smoother but less faithful.

**Index rate** — how strongly that index is applied. `0` = ignore the index,
`1` = follow it strictly. `0.75` is a typical middle value.

**Inference** — using a trained model to convert audio (as opposed to *training*
it).

## L

**Limiter** — stops audio from exceeding a loudness ceiling, preventing
clipping.

## M

**MelBand Roformer** — a family of neural models that separate vocals from
music. The `Kim FT` variants are the default picks here.

**Mix** — how much of an effect is blended in. `0` = none, `1` = all.

**Monitor Device** — a separate output you can listen to while changing your
voice live.

## N

**Noise Reduction** — removes hiss, hum and background noise. Strength controls
how aggressively.

**Normalization** — evening out the loudness of the audio.

## O

**Overlap length** — how much neighbouring training slices overlap so that no
word gets cut in half.

## P

**Pitch** — how high or low a voice sounds.

**Pitch shift (semitones)** — moves pitch up or down. `+12` = one octave up,
`-12` = one octave down, `0` = unchanged. Male→female typically `+12`.

**Post-Process** — apply the effect chain (reverb, delay, compressor, etc.)
after the voice conversion.

**Precision** (Applio Settings → Training) — numeric precision used during
training: `fp32` (safest), `fp16` (faster, less memory, can be unstable on CPU),
`bf16`.

**Pretrained** — a model that has already learned general voice conversion
before your training starts. Starting from one is much faster and needs less
data — recommended.

**Proposed Pitch** — the tool guesses the best pitch shift for your file. Use it
if you don't know what to set.

**Protect Voiceless Consonants** — keeps s/f/t/ch sounds crisp instead of
smeared. Raise it if speech sounds mushy.

## Q

**Quefrency (formant shifting)** — a fine-tuning value for how the formant shift
behaves. Adjust only after enabling Formant Shifting.

## R

**Reference audio** — a sample of the target voice, used by SVA (no training
needed). 5–15+ seconds of clean speech.

**Ref crop lengths** — trim the start of each reference clip to N seconds.

**Reverb** — the sound of a room. Sliders: **Room Size, Damping, Wet Gain,
Dry Gain, Width, Freeze Mode**.

**Room Size** — how big the simulated room sounds.

**rmvpe** — the recommended default pitch-detection method: fast and accurate,
and handles high voices well (with high-register correction on).

**RVC (Retrieval-based Voice Conversion)** — the Applio engine. You train a
model on a voice, then convert with it. Highest quality, needs training data.

## S

**Sampling Rate** — how many audio samples per second (e.g. 40000 Hz). Higher =
more detail, bigger files.

**Search Feature Ratio** — how hard the model tries to match the trained voice.
Higher = stricter match.

**Semitone** — one musical step. 12 semitones = one octave.

**Silent training files** — how much silence the trainer will tolerate in a
training file before discarding it.

**Simulate streaming** (SVA) — process the audio in stream-like chunks. Same
result, different internal path. Off for normal file work.

**Split Audio** — cut a file into parts, convert each, then join them. Helps
long audio.

**stem** — one separated layer of a mix: the *vocals* stem and the *music* stem.

**Stem separation** — the act of pulling those layers apart (what the music
remover does).

**Speaker ID** — which speaker to use when a model was trained on several.

**spin / spin-v2** — alternative embedder models. `contentvec` is the default.

**StreamVoiceAnon (SVA)** — zero-shot voice conversion: give it a sample of the
target voice and it converts immediately, no training.

**Sync** — not a setting here, but the goal: output words must line up with the
input words.

## T

**TensorBoard** — a graphs dashboard for watching training progress live.

**Timbre** — the *colour* of a voice: what makes two people sound different even
on the same note.

**TTS (Text to Speech)** — turning written text into spoken audio.

**TTS Voices** — the built-in neural text-reader voice used to create the base
speech before your model re-voices it.

## V

**VAD (Voice Activity Detection)** — only processes audio while you are actually
speaking. Saves work and avoids silence artefacts.

**Vocoder** — the part of the system that rebuilds the waveform. `HiFi-GAN` is
the default here, `RefineGAN` the alternative.

**Voice Model** — a trained model file (`.pth`) you convert with.

**Voice Blender** — mixing two trained models into one, by ratio.

**Volume Envelope** — how much of the original loudness shape is preserved.

## W

**Wet Gain** — the amount of effect-heavy sound in the mix. Opposite of dry.

**weights_only** — (not a UI setting; appears in internals) a safety flag when
loading model files. The workstation patches the loader so old models still
load correctly.

---

## Quick "if X then Y"

| The output sounds like the original speaker | Lower **Alpha** (SVA) / raise **Index rate** (Applio) |
| The voice sounds robotic | Raise **Index rate** down toward `0.3–0.5`; make sure **Protect Voiceless Consonants** is sane |
| The voice is too high/low | Change **Pitch shift** by semitones |
| It sounds male but should sound female (or vice versa) at the same pitch | Turn on **Formant Shifting**, try preset `m2f` / `f2m` |
| Music still audible in the converted voice | Run the music remover first, or use a slower separation model |
| Words are cut off at the ends | Increase **Overlap length** or enable **Split Audio** |
