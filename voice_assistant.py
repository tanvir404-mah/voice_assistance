import speech_recognition as sr
import subprocess
import pyttsx3  # Import pyttsx3 for text-to-speech
import datetime
import webbrowser
import requests

# Initialize recognizer and TTS engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()  # Initialize the speech engine

# Function to speak text
def speak(text):
    engine.say(text)
    engine.runAndWait()

def get_time():
    now=datetime.datetime.now()
    current_time=now.strftime("%I:%M %p")
    return f"Today is {current_time}"

def get_date():
    now=datetime.datetime.now()
    current_date=now.strftime("%B:%d %y")
    return f"Today is {current_date}"

def get_weather():
    api_key = "a61e281e9e5467da64001a36303236df"  # Replace with your API key
    city = "Rajbari"  # Replace with your city name
    url = f"http://api.openweathermap.org/data/2.5/weather?q={Rajbari}&appid={a61e281e9e5467da64001a36303236df}&units=metric"
    response = requests.get(url)
    data = response.json()

    if data["cod"] == 200:
        main = data["main"]
        weather_desc = data["weather"][0]["description"]
        temperature = main["temp"]
        return f"The weather in {city} is currently {weather_desc} with a temperature of {temperature}°C."
    else:
        return "Sorry, I couldn't get the weather data."


def listen_command():
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Listening for command...")
        audio = recognizer.listen(source)

        try:
            command = recognizer.recognize_google(audio).lower()
            print(f"Command received: {command}")
            speak(f"Command received: {command}")
            return command
        except sr.UnknownValueError:
            print("Sorry, I didn't understand that.")
            speak("Sorry, I didn't understand that.")
            return None
        except sr.RequestError as e:
            print(f"API error: {e}")
            speak(f"API error: {e}")
            return None

def execute_command(command):
    if 'enable firewall' in command:
        #print("Firewall would be enabled (Linux only).")
        speak("Firewall would be enabled (Linux only).")
    elif 'disable firewall' in command:
        #print("Firewall would be disabled (Linux only).")
        speak("Firewall would be disabled (Linux only).")
    elif 'what time is it' in command:
        time = get_time()
        print(time)
        speak(time)
    elif 'what is the date' in command:
        date = get_date()
        print(date)
        speak(date)
    elif 'open google' in command:
        print("Opening Google...")
        speak("Opening Google...")
        webbrowser.open("https://www.google.com")
    elif 'what is the weather' in command:
        weather = get_weather()
        print(weather)
        speak(weather)    
    else:
        #print("Unknown command.")
        speak("Unknown command.")

if __name__ == "__main__":
    while True:
        command = listen_command()
        if command:
            execute_command(command)
