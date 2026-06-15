import speech_recognition as sr
import webbrowser
import sys

r = sr.Recognizer()


def listen():
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source, duration=0.8)
        # add timeouts so it doesn't hang indefinitely
        try:
            audio = r.listen(source, timeout=5, phrase_time_limit=6)
        except sr.WaitTimeoutError:
            print("No speech detected (timeout).")
            return ""

    try:
        command = r.recognize_google(audio)
        print("You said:", command)
        return command.lower()

    except Exception as e:
        print("Error:", e)
        return ""


def handle_command(command: str) -> bool:
    """Return True to continue, False to exit."""
    if not command:
        return True

    if not any(w in command for w in ("om", "home", "ohm")):
        return True

    if "youtube" in command:
        print("Opening YouTube...")
        webbrowser.open("https://www.youtube.com")

    elif "google" in command:
        print("Opening Google...")
        webbrowser.open("https://www.google.com")

    elif "stop" in command:
        print("Goodbye!")
        return False

    else:
        print("Command not recognized")
    return True


def main() -> None:
    print("Starting assistant. Say 'om' (or 'home'/'ohm') to activate. Press Ctrl+C to quit.")
    try:
        while True:
            command = listen()
            if not handle_command(command):
                break
    except KeyboardInterrupt:
        print("\nInterrupted by user. Exiting.")
        sys.exit(0)


if __name__ == "__main__":
    main()