@echo off
REM ───────────────────────────────────────────────────
REM Change working directory to the directory of this script
REM ───────────────────────────────────────────────────
cd /d "%~dp0"

REM Now you’re in the script’s folder. Add your commands below:
echo Now running in: %CD%

python pytts.py
