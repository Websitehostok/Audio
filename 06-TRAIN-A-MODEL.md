# Training your first voice model (from ~10 minutes of voice) — step by step

This is the complete walkthrough: record 10 minutes → train a model → use it in
**every** tool, in **every** future session.

**Read the warning box below first — it saves people from losing a model.**

---

## ⚠️ The one thing to understand before you start

A trained model lives **inside the Kaggle session**. When the session ends
(enough time passes, or you stop it), **the model is wiped.**

The dataset mount is read-only, so the workstation cannot save your model into
the dataset for you.

**So the last step of every training run is: download the `.pth` + `.index` files.**

Do that, and you can re-upload them in ~30 seconds in any later session
(Applio → **Download** tab → drop the files). Skip it, and the training is gone.

---

## Before you record — what makes usable training audio

You need **clean speech from one person only**.

| Do this | Why |
|---------|-----|
| 10 minutes of continuous normal speech | This is the practical **minimum**. |
| 30–60 minutes if you can | Noticeably better voice match and stability. |
| Same room, same mic, same volume | Mismatched recordings confuse the model. |
| No music, no other voices, minimal noise | Background noise gets baked into the voice. |
| Speak naturally — read a book, say anything | Content doesn't matter, only consistency. |
| One WAV/MP3 file is fine | You don't have to split it yourself. |

If you only have **5 minutes**: it can work, but expect a weaker, less stable
voice. Use it, and go back to record more if you like the result.

---

## Step 1 — Start the workstation

Run the cell, wait ~15 minutes, and open the **Full Applio UI** link.

Everything below happens on that one page.

---

## Step 2 — Name and configure the model

Go to the **Training** tab.

### Model Settings accordion

| Setting | What to put |
|---------|-------------|
| **Model Name** | A short name with no spaces, e.g. `myvoice` |
| **Architecture** | Leave `RVC` |
| **Sampling Rate** | Leave `40000` |
| **Vocoder** | Leave `HiFi-GAN` |

### Advanced Settings accordion

| Setting | What to put |
|---------|-------------|
| **CPU Cores** | Leave as is (the default is fine on Kaggle) |
| **GPU Number** | Leave as is — you are on a GPU session |
| **GPU Information** | Check it says a GPU was found; that's it |

---

## Step 3 — Load your audio

Still in the **Training** tab:

1. Open the **Preprocess** accordion → tick **Dataset Creator**.
2. In the **Dataset Creator** accordion:
   - **Dataset Name** — pick something like `myvoice`
   - **Upload Audio Dataset** — upload your recording (a `.zip`, `.wav`, or `.mp3`)
3. In Dataset Creator's own **Advanced Settings** accordion:

| Setting | Recommended |
|---------|-------------|
| **Audio cutting** | `Automatic` (trims silence for you) |
| **Chunk length (sec)** | leave the default (~4 s) |
| **Overlap length (sec)** | leave the default (~0.3 s) |
| **Noise filter** | leave on if your recording has any hiss |
| **Noise Reduction** | leave on for room recordings |
| **Noise Reduction Strength** | leave default |
| **Normalization mode** | `pre` |

4. Press the **Preprocess** button.
5. **Preprocess output** should end without errors. If it errors, the usual cause
   is an unsupported audio format — convert to WAV and retry.

---

## Step 4 — Extract the features

Still in the **Training** tab → **Extract** accordion:

| Setting | Recommended |
|---------|-------------|
| **Pitch extraction algorithm** | `rmvpe` |
| **Embedder Model** | `contentvec` |
| **Silent training files** | leave default |
| **Custom Embedder** | leave off |

Press the **Extract** button. **Feature extraction output** confirms when done.

---

## Step 5 — Train

Still in the **Training** tab → **Training** accordion:

| Setting | What to put | Why |
|---------|-------------|-----|
| **Batch Size** | leave the default | Kaggle's GPU handles it |
| **Save Every Epoch** | **`5`** | You get a checkpoint every 5 epochs, so a good version is never far away |
| **Total Epoch** | start with **`50`** | For 10 minutes of data this is enough to judge quality. You can always train more. |
| **Pretrained** | **ON** | Starts from a model that already understands speech — dramatically better from little data |
| **Fresh Training** | OFF | Only for very large datasets |
| **Save Only Latest** | your choice | ON saves disk |
| **Save Every Weights** | OFF (unless you want every epoch's full model) | Uses a lot of disk |
| **Cache Dataset in GPU** | ON if it fits | Faster |
| **Checkpointing** | ON | Lets you resume if something drops |
| **Shutdown after finishing** | OFF for your first run | You probably still want the session |
| **Index Algorithm** | `Auto` | |

**Tick "I agree to the terms of use"** — it will not run otherwise.

Press the **Train** button and watch **Training output**.

**How long:** with 10 minutes of audio on a T4x2, expect roughly **10–30 minutes**.
With 30–60 minutes of data, longer.

**When to stop early:** watch **TensorBoard** (its own tab → the link it prints).
When the loss curve flattens and stops improving, the model has learned what it
can — more epochs just start to overfit.

---

## Step 6 — Export the model

Still in the **Training** tab → **Export Model** accordion:

| Setting | What to do |
|---------|-----------|
| **Exported Pth file** | choose the checkpoint you want (the highest epoch is usually best) |
| **Pth file** | pick the matching entry |
| **Exported Index File** | choose the index to export |
| **Index File** | pick the matching entry |

Press the export button. Your model now appears in the model dropdowns.

If the dropdowns still look empty, open **Settings → General** and tick
**Enable model/index list filter** (this also gives you the Filter box).

---

## Step 7 — ⬇ DOWNLOAD THE MODEL (do not skip)

This is the step that makes your training permanent.

1. Go to the **Download** tab.
2. Use **"Drop your .pth and .index files here"** (the upload area) — this is
   also where you upload them back in a future session.
3. Find your `.pth` and `.index` files in the output folder the training log
   names, and download them to your PC.

Keep both files together — the model needs both.

**Never end a session without doing this.**

---

## Step 8 — Use the model everywhere

Once exported, `myvoice` appears in the model dropdown of **every tool that
takes a voice model**:

| Where | What to select |
|-------|----------------|
| **Hub → Applio (RVC) tab** | **Voice model** → `myvoice` |
| **Applio → Inference → Single** | **Voice Model** → `myvoice` |
| **Applio → Inference → Batch** | same dropdown, convert a whole folder |
| **Applio → TTS** | **Voice Model** → `myvoice` (text spoken in your voice) |
| **Applio → Realtime → Model Settings** | **Voice Model** (only with a real mic) |
| **Applio → Voice Blender** | "Path to first model" / "Path to second model" → `myvoice` |
| **Applio → Model information** | **Path to Model** → `myvoice` (inspect it) |

Same model, all features. Train once, use everywhere.

---

## Step 9 — Using it in a *new* session (every time after)

1. Start the workstation as usual.
2. Open **Applio** → **Download** tab.
3. Drop your saved `.pth` and `.index` into **"Drop your .pth and .index files
   here"**.
4. They appear in all the dropdowns immediately.

That's the whole "every time" workflow — about 30 seconds per session, no
retraining.

---

## Realistic expectations

| Amount of training audio | What to expect |
|--------------------------|----------------|
| 5 minutes | Recognisably the voice, but thin and unstable. Experiment-level. |
| 10 minutes | Usable. Intelligible, decent match. The recommended starting point. |
| 30 minutes | Good. Much more stable across different phrases. |
| 60+ minutes | Very good. Reliable for production work. |

If the voice sounds warbly, robotic, or the wrong gender, see the
**"if X then Y"** table at the bottom of `05-GLOSSARY.md` — most of those are
fixes you apply at conversion time, not reasons to retrain.
