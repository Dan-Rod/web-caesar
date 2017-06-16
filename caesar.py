import string

'''create a caesar cipher to return an encrypted message from any user inputted string'''


#build a dictionary to store each letter and their corresponding number
alphaPosition = {"a":0, "A":0, "b":1, "B":1, "c":2, "C":2, "d":3, "D":3, "e":4, "E":4, "f":5, "F":5, "g":6, "G":6, "h":7, "H":7, "i":8, "I":8, "j":9, "J":9, "k":10, "K":10, "l":11, "L":11, "m":12, "M":12, "n":13, "N":13, "o":14, "O":14, "p":15, "P":15, "q":16, "Q":16, "r":17, "R":17, "s":18, "S":18, "t":19, "T":19, "u":20, "U":20, "v":21, "V":21, "w":22, "W":22, "x":23, "X":23, "y":24, "Y":24, "z":25, "Z":25}
#build a seperate dictionary with the opposite key/values
positionAlpha = {}
for k,v in alphaPosition.items():
    positionAlpha[v] = k

def alphabet_position(letter):
    #Return the cooresponding number for a single letter string
    #from the dictionary, return the value for each key in the string
    return alphaPosition[(letter)]

def rotate_character(char,rot):
        #Take a char and translate to respective interger
    if char.isalpha():
        alphabet = string.ascii_lowercase if char.islower() else string.ascii_uppercase
        char = alphabet[(alphabet_position(char) + rot) % len(alphabet)]
    return char

def rotate_string(text,rot):
    #loop through a message and return encrypted message after rotating characters
    cryptMessage = ""
    for c in text:
        if c.isalpha():
            cryptMessage += rotate_character(c,rot)
        else:
            cryptMessage += c
            
    return cryptMessage


def main():
    message = input("Type your message, please:\n")
    rotate = int(input("How many letters would you like to rotate by:\n"))
    print(encrypt(message,rotate))
    

if __name__ == "__main__":
    main()

