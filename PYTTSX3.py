import pyttsx3

engine = pyttsx3.init()

# Speech speed adjustment
rate = engine.getProperty('rate')
print('Default voice speed: {}'.format(rate))
engine.setProperty('rate', 220)

engine.setProperty('volume', 2.0) # Default is 1.0
volume = engine.getProperty('volume')

# Get a list of available voices
voices = engine.getProperty('voices')

# Set the voice to a "soft female" voice.
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

engine.say('Host: Number 5 on our list is our adorable dachshund. With its long body and expressive eyes, this little sausage attracts attention. ')
engine.runAndWait()