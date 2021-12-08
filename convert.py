import speech_recognition as sr

def main():
    sound = "file.mp3"
    r = sr.Recognizer()

    with sr.AudioFile(sound) as source:
        r.adjust_for_ambient_noise(source)
        print("Converting Audio File to Text...")
        audio = r.listen(source)

        yes = ["yes", "ye", "yo", "yah", "y", "yup"]
        no = ["no", "nah", "nope", "n", "not"]

        choice = input().lower()
        if choice is yes:
           try:
               print("Converted Audio As : \n " + r.recognize_google(audio))

           except Exception as i:
               with open('output.txt', 'w') as f:
                   f.write("balance %d" % balance)
        elif choice is no:
           try:
               print("Converted Audio As : \n " + r.recgnonize_google(audio))

           except Exception as j:
               print(j)
        else:
           sys.stdout.write("Please Enter (Y/N) to Continue")

if __name__ == "__main__":
    main()
