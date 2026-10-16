# StreamVoiceAnon (SVA) — every setting explained

This is the same conversion engine as the Hub's first tab, but **every option is
exposed** and there is no second tab — this page does one thing: convert your
audio into a target voice, with no training required.

API it exposes: `/_convert`

---

## Inputs

| Setting | What you put in | What it means |
|---------|----------------|---------------|
| **Source audio (your voice)** | Audio file or mic recording | The speech whose *words* you keep. The voice gets replaced. |
| **Reference audio(s) — target voice** | One or more audio files | The voice you want to sound like. Use 5–15+ seconds of clean speech per file. More references = more stable voice. Background noise in a reference hurts the result badly. |

---

## Settings

| Setting | Type | Default | What it means |
|---------|------|---------|---------------|
| **Alpha (1.0 = keep voice, lower = more anonymization)** | Slider | `1.0` | Controls how much the *original speaker* is preserved. At `1.0` the output keeps as much of the source speaker's characteristics as possible — closest to natural, least change to the speaking identity. **Lowering it forces the output further from the source speaker**, so the privacy/anonymization effect is stronger. |
| **Simulate streaming** | Checkbox | Off | Processes audio in stream-like chunks instead of one whole-file pass. Used when you care how the voice behaves for live/streaming use. Same logic, different chunking — leave off for offline files. |
| **Ref crop lengths (seconds, optional, space-separated)** | Text | empty | Trims the start of each reference to N seconds. One number = trim all references to that length; several space-separated numbers = trim each file to its own length (e.g. `10 8 12`). Handy to cut leading silence/noise. Empty = use whole files. |
| **Pipeline config (VC)** | Dropdown | `configs/config_firefly_arvcasr_8192_delay0_8.yaml` | Model blueprint. **Stick to the default.** |
| **Checkpoint — dual_ar_* = conversion model** | Dropdown | `pretrained_checkpoints/dual_ar_delay_0_8.pth` | The trained weights. **Stick to the default** — the other three are supporting parts of the system, not alternatives to it. |

---

## Outputs

| Output | What it is |
|--------|------------|
| **Output** | The converted audio — play or download. |
| **Status** | Progress and plain-text errors. |

---

## Choosing Alpha — a quick reference

| You want | Alpha |
|----------|-------|
| Keep the source speaker's mannerisms, most natural result | `1.0` |
| Balanced | `0.7` |
| Clearly a different speaker | `0.4` |
| Maximum separation from the source speaker | `0.1` – `0.2` |

Note that pushing Alpha too low can reduce audio quality and intelligibility —
the tool has less of the original voice to work from. If it sounds robotic,
raise it back up.

---

## Reference audio — what makes a good one

- Clean speech, no music, no background noise.
- The person speaking normally (not shouting, not whispering).
- At least 5–15 seconds; longer is better up to a point.
- If you use several, put the best one first.
- Use **Ref crop lengths** to cut silent or noisy beginnings.
