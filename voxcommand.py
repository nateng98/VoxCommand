import speech_recognition as sr
# from pynput.keyboard import Key, Controller
from pynput.mouse import Button, Controller
from pynput import mouse

voiceRecognizer = sr.Recognizer()
# config
voiceRecognizer.energy_threshold = 300
voiceRecognizer.pause_threshold = 1
voiceRecognizer.dynamic_energy_threshold = False
print(sr.Microphone.list_microphone_names()) # see which index is your desired device to use as microphone

keyboard = Controller()
mouse = Controller()

# Testing voice input
def capturing_voice():
  # Choose the device you want to use as microphone
  with sr.Microphone(device_index=1) as mic:
    print('Listening...')
    audio = voiceRecognizer.listen(mic)
  return audio

# Converting audio to text
def audio_to_text(audio):
  try:
    text = voiceRecognizer.recognize_google(audio) # using google web speech API
    print('You said: ' + text.lower())
  except sr.UnknownValueError:
    text = ''
    print('Sorry, I did not quite catch that.')
  except sr.RequestError as e:
    text = ''
    print('Error; {0}'.format(e))
  return text.lower()

# Processing command
# Change or add any command you want
def processing_command(text):
  if 'hey vox' in text:
    print('Hii my beloved Nathan! How can I please you?')

# Mouse key 4
  elif 'switch' in text:
    mouse.press(Button.x1)
    mouse.release(Button.x1)
    print('Mouse 4 pressed')
# Mouse key 5
  elif 'auto attack' in text:
    mouse.press(Button.x2)
    mouse.release(Button.x2)
    print('Mouse 5 pressed')
    
  elif 'goodbye vox' in text:
    print('Goodbye my beloved Nathan! I will see you again')
    return True
  else:
    print('I did not quite catch that. Can you repeat that for me, my love?')
    return False
  
# Main
def main():
  exit_script = False
  while not exit_script:
    audio = capturing_voice()
    text = audio_to_text(audio)
    exit_script = processing_command(text)
    
if __name__ == "__main__":
  main()