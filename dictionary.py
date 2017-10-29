import json

data = json.load(open("data.json"))

#Looks for word in data.json file (dictionary file)
def dictionary(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif(w == "all star"):
        return("Hey, now, you're an All Star")
    elif(w == "cryus" || w == "Cyrus")
        s = Sound()
        s.read("memes.mp3")
        s.play()
        return("ARE YOU FEELING THE MEMES?")
    else:
        return("Not found in dictionary.")

#Runs terminal version of program
def main():
    wIn = input("What word do you want to know about?")
    print(str(dictionary(wIn)))


#If file is run as standalone, run main() function
if __name__ == "__main__":
    main()
