# VoxCommand
**VoxCommand** is a voice-controlled python script that enables users to effortlessly trigger specific key commands or combinations through intuitive voice commands.

### Backstory
When my right thumb was sidelined by a fracture, I found myself unable to execute the mouse key 4 *(switching weapons)* and  mouse key 5 *(auto attacking)*, which were essential for playing my favorite MMORPG, Guild Wars 2. Frustrated by this limitation, I set out to develop **VoxCommand** — a voice-controlled solution that allowed me to seamlessly trigger those commands without relying on my injured thumb. What began as a personal quest for accessibility in gaming turned into VoxCommand, a tool that empowers users facing similar "challenges" to press a certain button or combination of buttons using simple voice commands.

## Requirements

1. Install SpeechRecognition
`pip install SpeechRecognition`

2. Install PyAudio
`pip install PyAudio`

3. Install pynput
`pip install pynput`

## Config
### Select device:
Change `device_index` that corresponds to your desired microphone in `sr.Microphone(device_index=1)`

```py
def capturing_voice():
  with sr.Microphone(device_index=1) as mic:
    print('Listening...')
    audio = voiceRecognizer.listen(mic)
  return audio
```
If you're not sure what the index of your microphone is, uncomment `line 11`
```py
print(sr.Microphone.list_microphone_names())
```
and run the script. It will print out the list of all microphones on your system. Choose your device from that list (starting index is 0).

### Commands:
Change text within single quotation ' ' to your command

- For mouse:
```py
elif 'auto attack' in text:
    mouse.press(Button.x2)
    mouse.release(Button.x2)
```
- For keyboard:
```py
elif 'ultimate' in text:
    keyboard.press('f')
    keyboard.release('f')
```

### Note:
- If you are using mouse with few extra keys like MMO mouse, there're some buttons that are not specified. To find out the name of the button, run `python findButtonName.py` Everytime you click, it prints out button's name.

Example: If I click mouse left, mouse 5 and mouse 4 in order, the output will be:
```
Button.left
Button.x2   
Button.x1   
```

## Usage

Run script `python voxcommand.py`

The console will show this as indication asking for input
```
Listening...
```

Example output:
```
Listening...
You said: auto attack
Mouse 5 pressed
```

### Author

[Nước Mắm Code](https://github.com/nateng98)