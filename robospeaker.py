import pyttsx3

print("Welcome To robo speaker")

# Initialize the text-to-speech engine
jarvis = pyttsx3.init()

while True:
    x = input("Enter what you want me to say (type 'q' to quit): ")

    if x == "q":
        jarvis.say('goodbye')
        jarvis.runAndWait()
        break

    jarvis.say(x)
    jarvis.runAndWait()

# Properly terminate the engine when done
jarvis.stop()
jarvis.quit()
