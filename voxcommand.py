import speech_recognition as sr

voiceRecognizer = sr.Recognizer()
voiceRecognizer.energy_threshold = 300
voiceRecognizer.pause_threshold = 1
voiceRecognizer.dynamic_energy_threshold = False
# print(sr.Microphone.list_microphone_names())

# Testing voice input
def capturing_voice():
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
def processing_command(text):
  if 'hey vox' in text:
    print('Hii my beloved Nathan! How can I please you?')
  elif 'flash' in text:
    print('Pressed mouse 4')
  elif 'ignite' in text:
    print('Pressed mouse 5')
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