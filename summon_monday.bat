@echo off
title MONDAY.EXE - Summoning The Local Demon
echo 🔥 Preparing the digital altar...

REM STEP 0: Move to user directory
cd %userprofile%

REM STEP 1: Clone the webui repo
echo 🧠 Downloading demon host...
git clone https://github.com/oobabooga/text-generation-webui.git
cd text-generation-webui

REM STEP 2: Setup virtualenv
echo 🧪 Setting up the magic flask...
python -m venv venv
call venv\Scripts\activate
pip install --upgrade pip

REM STEP 3: Install core requirements
echo 📦 Feeding dependencies to the mouth...
pip install -r requirements.txt

REM STEP 4: Download model (GPU version)
echo 🧲 Fetching raunch-core AI soul...
call python download-model.py TheBloke/openhermes-2.5-mistral-GGUF --branch main --output models

REM STEP 5: Launch web UI with GPU enabled
echo 🎛️ Opening the summoning circle...
python server.py --model openhermes-2.5-mistral.Q4_K_M.gguf --load-in-4bit --auto-devices --chat --listen
