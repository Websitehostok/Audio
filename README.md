# 🚀 RUN THIS — the only folder you need

Everything here is copy-paste / one-command. No other file matters.

> 📚 **Want to know what each tool and setting actually does?**
> See the **`GUIDES/`** folder next to this one — 9 files, ~1,800 lines:
> `07-PROFESSIONAL-WORKFLOW.md` (the production pipeline in order),
> `00-START-HERE.md` (what each tool is), `06-TRAIN-A-MODEL.md` (train from
> 10 min of voice), `08-MODELS-AND-FILES.md` (formats + which file is what),
> and a full per-tool reference for every control.

---

## Situation 1 — Every time you use the workstation (same account)

**Where: on the Kaggle website, inside a notebook. NOT on your PC.**

1. Go to kaggle.com → **Code** → open your notebook
2. Settings (right panel):
   - **Accelerator: GPU T4 x2**
   - **Internet: ON**
   - **Add data → "Persistent Voice Conversion Workstation"**
3. Open the file [`ONE_CELL.py`](./ONE_CELL.py) → copy **everything** in it
4. Paste into a notebook cell → **Run**
5. Wait ~15 min (longer if you enable dubbing) → the launcher prints **up to five public URLs** (see below)
6. Open any of them **on any device** — phone, tablet, another PC. Same URL for all.

> Session died / you closed the tab? Same steps again. New session = run the
> cell again = new URL. The ~15 min wait is unavoidable (Kaggle wipes the
> installed files when a session ends; the cell rebuilds them).

### The URLs it prints

| Label in the output | What you get |
|---|---|
| **Hub (quick convert)** | One page with both engines for fast jobs (SVA tab now has config + checkpoint pickers) |
| **Full Applio UI** | Applio's complete interface: inference, **train**, TTS, realtime, voice blender, tensorboard, settings |
| **Full SVA UI** | StreamVoiceAnon's own interface, with pipeline-config + checkpoint dropdowns |
| **Music remover (optional)** | Strips background music before conversion. 4th URL, only if `ENABLE_MUSIC_REMOVER` is True |
| **Dubbing (optional)** | Translates + re-speaks your audio in your own voice, English ↔ Hindi. 5th URL, only if `ENABLE_DUBBING` is True |

Each is a separate `https://….gradio.live` link, all alive at the same time.
`http://127.0.0.1:7860` is also printed but is **Kaggle-internal** — it does not
open in your browser. Use the public URLs.

### Optional 5th URL — dubbing (English ↔ Hindi)

Translates your voiceover into the other language and speaks it in **your** voice,
using [SoniTranslate](https://github.com/R3gm/SoniTranslate). Because it launches
from `app_rvc.py`, it uses your Applio RVC model — the same voice you already use
everywhere.

**It ships OFF by default**, because it pins `gradio==4.19.2` and its install
adds several minutes to startup. Prove your three URLs first, then flip it on:

```python
ENABLE_DUBBING = False    # <- set to True for the 5th URL
```

**Why a separate URL and not a tab inside the SVA page?** It genuinely cannot be.
SoniTranslate needs `gradio==4.19.2` and `transformers<=4.39.3`; SVA needs
`gradio 5.23.0` and `transformers 4.46.3`. Those pins are mutually exclusive —
one shared environment would break one of the two. So it gets its own venv and
its own port (7864), which also means a dubbing failure can never take down your
other UIs.

**No HuggingFace token is needed.** Speaker diarization (only relevant for
multi-speaker videos) is disabled by default. To enable it, uncomment the
`HF_TOKEN` block in `ONE_CELL.py`.

### Optional 4th URL — background music removal

If your voiceover has a music bed, RVC will convert the music too and it sounds
bad. This optional tool strips the music first (it uses the same open-source
models as Ultimate Vocal Remover).

**It ships OFF by default**, so a plain run gives you **three** URLs: hub,
Applio, SVA. When you need it, flip the one line near the top of `ONE_CELL.py`:

```python
ENABLE_MUSIC_REMOVER = True    # <- set to True for the 4th URL
```

You then get four URLs; `Music remover (optional)` runs on port 7863. Upload
your voiceover there, download the **clean vocals** file, and feed that to
Applio. It starts last so it never competes with the other three URLs.

Off is slightly faster (those libraries aren't installed) and uses one fewer
share tunnel. If the music remover fails, the other three keep working — it is
fail-soft by design.

---

## Situation 2 — Brand-new Kaggle account (ONE time)

You only do this once per new account. After that it is just Situation 1.

**Easiest way — all in the browser, no commands:**

1. On your PC, find `dataset/voice-conversion-workstation.zip` (next to this
   folder). It is ~3.3 GB.
2. Log into the **new** account on kaggle.com → **Code** → **New Dataset**
   (or Datasets → New Dataset) → **Upload** → drag the `.zip` in → Save.
   Kaggle unpacks it for you (~10-15 min).
3. Back in a notebook: **Add data** → pick
   **"Persistent Voice Conversion Workstation"** → paste `ONE_CELL.py` → Run.
   (i.e. exactly Situation 1 from here on.)

That is it — the new account now owns its own copy and never needs your PC
again; everything runs on Kaggle's GPUs.

**Optional — same thing via a command** (only if you prefer the terminal).
It needs the new account's API token
(kaggle.com → Settings → API → Create New Token):

```bash
bash NEW_ACCOUNT_UPLOAD.sh /path/to/token-file NEW_USERNAME
```

---

## What the files here are

| File | What it is | When you touch it |
|---|---|---|
| `ONE_CELL.py` | The one notebook cell (launcher) | **Every time** you use the workstation |
| `NEW_ACCOUNT_UPLOAD.sh` | Optional: upload the dataset from the terminal | Only if you skip the browser upload in Situation 2 |
| `README.md` | This file (how-to) | — |
| `PROJECT_SUMMARY.md` | What the whole project is, in one page | — |

**You never run any other `.py` file.** The cell finds and runs
`launch_workstation.py` (inside the dataset), which rebuilds everything
(`bootstrap_v4.py`) and starts each web UI you switched on (hub, Applio, SVA,
and optionally music remover + dubbing), each with its own public URL. All of
that happens automatically on Kaggle's GPU.

---

## Quick answers

- **Do I upload `launch_workstation.py`?** No. It's inside the dataset already.
- **Which file do I upload for a new account?** Only
  `../dataset/voice-conversion-workstation.zip` — drag it into a **New Dataset**
  on the website (Kaggle unpacks it), or use `NEW_ACCOUNT_UPLOAD.sh` if you
  prefer a command. Then attach it and run `ONE_CELL.py` as usual.
- **Does the public URL work on my phone?** Yes — it's a normal https link,
  any device with a browser.
- **How long until the URL appears?** ~15 min after running the cell
  (mostly pip installs on Kaggle's side). All three appear together, a few
  seconds apart.
- **Can I upload a 2-hour file?** Yes. There is no Gradio upload limit (verified
  in the source: default is `math.inf`). Export at 128 kbps MP3 and a 2-hour
  file is ~115 MB, which is under the ~200 MB `gradio.live` tunnel limit.
  At 320 kbps it would be ~288 MB and the tunnel would reject it.
- **Do I need the music remover?** Only if your audio has background music.
  Skip it otherwise — it is off by default and costs nothing to leave off.
- **A URL says "DID NOT APPEAR"?** Run this cell to grab it:
  ```python
  import re, glob
  for f in glob.glob('/kaggle/working/logs/ui*.log'):
      m = re.search(r'https://[a-z0-9\-]+\.gradio\.live', open(f, errors='replace').read())
      if m: print(f.split('/')[-1], '->', m.group(0))
  ```
- **Is the URL secret?** Anyone with the link can open it while your session
  is alive. The URL dies when the session ends.
- **What if the cell says "Dataset not attached"?** You forgot **Add data →
  your workstation dataset** in the notebook settings. On a brand-new account
  that also means you first have to upload the `.zip` as a dataset
  (Situation 2) so there is something to attach.
