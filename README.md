# VoxCommand
**VoxCommand** is a voice-controlled python script that enables users to effortlessly trigger specific key commands or combinations through intuitive voice commands.

### Backstory
When my right thumb was sidelined by a fracture, I found myself unable to execute the mouse key 4 *(switching weapons)* and  mouse key 5 *(auto attacking)*, which were essential for playing my favorite MMORPG, Guild Wars 2. Frustrated by this limitation, I set out to develop **VoxCommand** — a voice-controlled solution that allowed me to seamlessly trigger those commands without relying on my injured thumb. What began as a personal quest for accessibility in gaming turned into VoxCommand, a tool that empowers users facing similar "challenges" to press a certain button or combination of buttons using simple voice commands.

### Requirements

*Note: Microphone() will not work if you run in virtual environment. OpenAI Whisper only supports Python 3.8-3.11, so either your version has to be 3.8-3.11 or have 3.8-3.11 installed with pyenv*

1. Enable running scripts on your system

*You can skip first 3 steps if you already have 3.8-3.11 version installed*
```bash
Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Unrestricted
```

2. Install pyenv-win PowerShell

```bash
Invoke-WebRequest -UseBasicParsing -Uri "https://raw.githubusercontent.com/pyenv-win/pyenv-win/master/pyenv-win/install-pyenv-win.ps1" -OutFile "./install-pyenv-win.ps1"; &"./install-pyenv-win.ps1"
```
3. Reopen PowerShell
```bash
pyenv install 3.11.0
```
Refer to [pyenv for Windows](https://github.com/pyenv-win/pyenv-win) if you have any problems

4. Install SpeechRecognition and PyAudio
```bash
pip install SpeechRecognition
pip install PyAudio
```
