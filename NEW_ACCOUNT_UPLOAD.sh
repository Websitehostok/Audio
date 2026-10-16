#!/usr/bin/env bash
# ============================================================
#  ONE-TIME: upload the workstation dataset to a NEW Kaggle account
#  Run this ON YOUR PC, from this folder:
#
#      bash NEW_ACCOUNT_UPLOAD.sh /path/to/token-file NEW_USERNAME
#
#  You need:
#    1. The new account's API token file (kaggle.com -> Settings ->
#       API -> Create New Token). It downloads as a file named "api"
#       or "kaggle.json".
#    2. Your new account's USERNAME.
#
#  The dataset zip is taken from ../dataset/voice-conversion-workstation.zip
# ============================================================
set -e

TOKEN_FILE="$1"
USERNAME="$2"

if [ -z "$TOKEN_FILE" ] || [ -z "$USERNAME" ]; then
  echo "Usage: bash NEW_ACCOUNT_UPLOAD.sh /path/to/token-file NEW_USERNAME"
  echo "  token file: kaggle.com -> Settings -> API -> Create New Token"
  exit 1
fi

if [ ! -f "$TOKEN_FILE" ]; then
  echo "ERROR: token file not found: $TOKEN_FILE"
  exit 1
fi

ZIP="../dataset/voice-conversion-workstation.zip"
if [ ! -f "$ZIP" ]; then
  echo "ERROR: $ZIP not found. Run this script from the RUN_THIS folder."
  exit 1
fi

# ---- 1. install kaggle CLI if missing ----
if ! command -v kaggle >/dev/null 2>&1; then
  echo "[1/5] Installing kaggle CLI..."
  pip install --user kaggle
else
  echo "[1/5] kaggle CLI found."
fi

# ---- 2. install the NEW account's token ----
echo "[2/5] Installing new account token (old token is backed up)..."
if [ -f "$HOME/.kaggle/access_token" ]; then
  cp "$HOME/.kaggle/access_token" "$HOME/.kaggle/access_token.bak"
fi
mkdir -p "$HOME/.kaggle"
cp "$TOKEN_FILE" "$HOME/.kaggle/access_token"
chmod 600 "$HOME/.kaggle/access_token"

# ---- 3. roomy TMPDIR (Kaggle CLI zips into TMPDIR before upload;
#         default /tmp is too small and the upload dies) ----
export TMPDIR="$HOME/tmp"
mkdir -p "$TMPDIR"

# ---- 4. extract zip + write metadata for the NEW account ----
echo "[3/5] Extracting dataset zip (~3.3 GB, takes a minute)..."
WORK="$(mktemp -d "$TMPDIR/ws_upload_XXXXXX")"
unzip -q "$ZIP" -d "$WORK"
cat > "$WORK/dataset-metadata.json" <<EOF
{
  "title": "Persistent Voice Conversion Workstation",
  "id": "$USERNAME/voice-conversion-workstation",
  "licenses": [{ "name": "CC0-1.0" }]
}
EOF

# ---- 5. upload ----
echo "[4/5] Uploading to Kaggle as $USERNAME (10-15 min, ~3.3 GB)..."
echo "      You will see several 'Upload successful' lines - wait for ALL of them."
kaggle datasets create -p "$WORK" --dir-mode zip

echo "[5/5] DONE."
echo ""
echo "Next steps (on kaggle.com, in a browser):"
echo "  1. New Notebook -> Settings -> Accelerator: GPU T4 x2, Internet: ON"
echo "  2. Add data -> your 'Persistent Voice Conversion Workstation'"
echo "  3. Paste the contents of ONE_CELL.py into a cell and Run"
echo "  4. Wait ~15 min -> open the printed public gradio.live URL on any device"
echo ""
echo "NOTE: your previous Kaggle token (if any) was backed up to"
echo "      ~/.kaggle/access_token.bak - restore it to push datasets as the old account."
