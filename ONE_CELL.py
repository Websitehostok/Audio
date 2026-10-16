# ============================================================
#  THE ONLY CELL YOU EVER RUN
#  Paste this into a Kaggle notebook cell and press Run.
#
#  Works in ALL three situations, same cell every time:
#    * Same account, new session  -> attach the dataset, Run (~15 min)
#    * Same account, live session -> just Run again (~2-3 min)
#    * Brand-new Kaggle account   -> upload the workstation .zip as a
#                                    dataset once, attach it, Run
#
#  Notebook settings (right panel) MUST be:
#    - Accelerator: GPU T4 x2
#    - Internet: ON
#    - Add data -> your workstation dataset (or the uploaded zip's dataset)
#
#  Public https://...gradio.live URLs get printed at the end.
#  Open them on ANY device (phone / PC / tablet).
# ============================================================
import glob, os, runpy, zipfile

# ============================================================
#  SWITCHES  --  set True / False, then Run All
# ============================================================
#  Each True starts that tool AND installs its libraries.
#  Each False skips it completely, so it is not installed and no
#  URL is printed for it. Fewer tools True = faster startup.
#
#  Start with everything False except APPLIO and SVA, confirm those
#  work, then switch on the extras one at a time.
# ------------------------------------------------------------

# 1) HUB -- the combined "quick convert" page (both engines).
#    Recommended: always True. It is your main landing page.
ENABLE_HUB = True

# 2) FULL APPLIO UI -- train a voice model, inference, TTS,
#    realtime, voice blender. This is where you TRAIN your model.
ENABLE_APPLIO = True

# 3) FULL SVA UI -- StreamVoiceAnon, zero-shot voice cloning.
#    Use this for quick conversions without training anything.
ENABLE_SVA = True

# 4) MUSIC REMOVER -- strips background music from a voiceover
#    before conversion. English/Hindi or any language.
ENABLE_MUSIC_REMOVER = False

# 5) DUBBING -- translates your audio and speaks it in your own
#    voice. English <-> Hindi. Slowest to install; leave off
#    until the other four are proven.
ENABLE_DUBBING = False

# ============================================================
#  HUGGINGFACE TOKEN (optional)
# ============================================================
#  Only needed for MULTI-SPEAKER videos. Speaker diarization is
#  turned OFF by default, so leave this alone unless you need to
#  tell apart several different speakers in one video.
#
#  Get a token at https://huggingface.co/settings/tokens (Role: Read)
#  and accept the licences on:
#    https://huggingface.co/pyannote/speaker-diarization
#    https://huggingface.co/pyannote/segmentation
#
# HF_TOKEN = "hf_xxxxxxxxxxxxxxxxxxxx"
# if HF_TOKEN:
#     os.environ["HF_TOKEN"] = HF_TOKEN
# ============================================================


def _flag(value):
    """True/False -> '1'/'0' for the launcher's env-var switches."""
    return "1" if value else "0"


os.environ["WS_WITH_HUB"] = _flag(ENABLE_HUB)
os.environ["WS_WITH_APPLIO"] = _flag(ENABLE_APPLIO)
os.environ["WS_WITH_SVA"] = _flag(ENABLE_SVA)
os.environ["WS_WITH_SEP"] = _flag(ENABLE_MUSIC_REMOVER)
os.environ["WS_SONITRANSLATE"] = _flag(ENABLE_DUBBING)


def _find_launcher():
    """Locate launch_workstation.py inside whatever data is attached.

    Kaggle usually mounts a dataset as an extracted tree, so the launcher is
    already a plain file. If it is not found (e.g. the data was attached as a
    raw .zip that Kaggle did not unpack), fall back to extracting the first
    attached zip that contains the launcher, then search again.
    """
    hits = glob.glob('/kaggle/input/**/launch_workstation.py', recursive=True)
    if hits:
        return sorted(hits)[0]
    for z in glob.glob('/kaggle/input/**/*.zip', recursive=True):
        try:
            with zipfile.ZipFile(z) as zf:
                if not any(n.endswith('launch_workstation.py') for n in zf.namelist()):
                    continue
                dest = '/kaggle/working/_ws_extract'
                print('Launcher not mounted as a file; extracting', z, '->', dest)
                os.makedirs(dest, exist_ok=True)
                zf.extractall(dest)
        except Exception as e:
            print('  skipped', z, '->', repr(e))
            continue
        hits = glob.glob(dest + '/**/launch_workstation.py', recursive=True)
        if hits:
            return sorted(hits)[0]
    return None


launcher = _find_launcher()
print('Found launcher:', launcher)
assert launcher, ('Dataset not attached -- use Add data -> your workstation '
                  'dataset (upload the workstation .zip as a dataset if you '
                  'do not have one yet)')

wanted = [n for n, v in (
    ("Hub", ENABLE_HUB), ("Applio", ENABLE_APPLIO), ("SVA", ENABLE_SVA),
    ("Music remover", ENABLE_MUSIC_REMOVER), ("Dubbing", ENABLE_DUBBING)) if v]
print('URLs you asked for:', ', '.join(wanted) if wanted else '(none)')
print('URLs you will get  :', len(wanted))
print('Expected wait: ~15 min for 2-3 tools, longer with music remover/dubbing.')
print('-' * 60)

# The assignment matters: a bare runpy.run_path(...) as the last cell line makes
# Jupyter echo the whole launcher module namespace (a huge unusable dict).
_ = runpy.run_path(launcher, run_name='__main__')