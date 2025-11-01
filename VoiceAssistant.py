# Voice Assistant - Advanced Version with Streaming and Websites
import speech_recognition as sr
import datetime
import subprocess
import pywhatkit
import pyttsx3
import webbrowser
import wikipedia
import pyjokes
import sys

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
recognizer = sr.Recognizer()

def talk(text):
    print(text)
    engine.say(text)
    engine.runAndWait()

def cmd():
    with sr.Microphone() as source:
        print("Clearing background noises... Please wait")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        print("Ask me anything...")
        recordedaudio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(recordedaudio, language='en_US')
        text = text.lower()
        print("Your message:", format(text))

        # --- 1️⃣ Open Chrome ---
        if 'chrome' in text:
            talk('Opening Chrome...')
            programName = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            subprocess.Popen([programName])

        # --- 2️⃣ Tell Time ---
        elif 'time' in text:
            time = datetime.datetime.now().strftime('%I:%M %p')
            talk(f"The time is {time}")

        # --- 3️⃣ Play YouTube Video ---
        elif 'play' in text:
            talk('Playing on YouTube...')
            pywhatkit.playonyt(text)

        # --- 4️⃣ Open YouTube ---
        elif 'youtube' in text:
            talk('Opening YouTube...')
            webbrowser.open('https://www.youtube.com')

        # --- 5️⃣ Google Search ---
        elif 'google' in text:
            talk('Searching Google...')
            pywhatkit.search(text)

        # --- 6️⃣ Wikipedia Summary ---
        elif 'wikipedia' in text:
            talk('Searching Wikipedia...')
            try:
                result = wikipedia.summary(text.replace('wikipedia', ''), sentences=2)
                talk(result)
            except:
                talk("Sorry, I couldn't find anything on Wikipedia.")

        # --- 7️⃣ Weather ---
        elif 'weather' in text:
            talk('Opening weather updates...')
            webbrowser.open('https://www.google.com/search?q=weather')

        # --- 8️⃣ Tell a Joke ---
        elif 'joke' in text:
            joke = pyjokes.get_joke()
            talk(joke)

        # --- 9️⃣ Exit Command ---
        elif 'stop' in text or 'exit' in text or 'quit' in text:
            talk("Goodbye! Have a great day.")
            sys.exit()

        # --- 🔟 Open LinkedIn ---
        elif 'linkedin' in text:
            talk("Opening LinkedIn...")
            webbrowser.open('https://www.linkedin.com')

        # --- 11️⃣ Open GitHub ---
        elif 'github' in text:
            talk("Opening GitHub...")
            webbrowser.open('https://www.github.com')

        # --- 12️⃣ Open Gmail ---
        elif 'gmail' in text:
            talk("Opening Gmail...")
            webbrowser.open('https://mail.google.com')

        # --- 13️⃣ Open Netflix or Play a Show ---
        elif 'netflix' in text:
            talk("Opening Netflix...")
            webbrowser.open('https://www.netflix.com')
            # Optional: Play something specific if mentioned
            if 'play' in text:
                movie = text.replace('play', '').replace('on netflix', '').strip()
                if movie:
                    talk(f"Searching for {movie} on Netflix.")
                    webbrowser.open(f"https://www.netflix.com/search?q={movie}")

        # --- 14️⃣ Open Amazon Prime or Play Something ---
        elif 'amazon' in text or 'prime video' in text:
            talk("Opening Amazon Prime Video...")
            webbrowser.open('https://www.primevideo.com')
            if 'play' in text:
                movie = text.replace('play', '').replace('on amazon', '').strip()
                if movie:
                    talk(f"Searching for {movie} on Amazon Prime Video.")
                    webbrowser.open(f"https://www.primevideo.com/search/ref=atv_sr_sug_1?phrase={movie}")

        else:
            talk("Sorry, I didn’t catch that. Please try again.")

    except Exception as ex:
        print(ex)
        talk("Sorry, I couldn’t understand that.")

# --- Continuous Listening Loop ---
while True:
    cmd()
