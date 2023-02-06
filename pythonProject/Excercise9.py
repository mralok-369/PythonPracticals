# Akhbaar padhke sunaao
# Attempt it yourself and watch the series for solution and shoutouts for this lecture!
def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVoice")
    speak.__call__(str)

if __name__ == '__main__':
    speak("You are the best my friend");