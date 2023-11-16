# VoxCommand
**VoxCommand** is a voice-controlled python script that enables users to effortlessly trigger specific key commands or combinations through intuitive voice commands.

### Backstory
When my right thumb was sidelined by a fracture, I found myself unable to execute the mouse key 4 *(switching weapons)* and  mouse key 5 *(auto attacking)*, which were essential for playing my favorite MMORPG, Guild Wars 2. Frustrated by this limitation, I set out to develop **VoxCommand** — a voice-controlled solution that allowed me to seamlessly trigger those commands without relying on my injured thumb. What began as a personal quest for accessibility in gaming turned into VoxCommand, a tool that empowers users facing similar "challenges" to press a certain button or combination of buttons using simple voice commands.

### Requirements

#### Note: 
- Microphone() will not work if you run in virtual environment. OpenAI Whisper only supports Python 3.8-3.11, so either your version has to be 3.8-3.11 or have 3.8-3.11 installed with pyenv

[How to install pyenv on windows](https://github.com/pyenv-win/pyenv-win)

[How to install chocolatey](https://docs.chocolatey.org/en-us/choco/setup)

#### Installation

1. Install ffmpeg
```bash
choco install ffmpeg
```

2. Install OpenAI Whisper
```bash
pip install -U openai-whisper
```

3. Install SpeechRecognition and PyAudio
```bash
pip install SpeechRecognition
pip install PyAudio
```

