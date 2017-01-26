def alphabet_position(letter):
    letter = ord(letter.lower()) - 97
    return letter

def rotate_character(char,rot):
    if not char.isalpha():
        return char
    if char.isupper():
        pos = alphabet_position(char)
        newchar = pos + rot
        if newchar > 25:
            newchar = newchar % 26
        shifted = chr(newchar+65)
        return shifted

    if char.islower():
        pos = alphabet_position(char)
        newchar = pos + rot
        if newchar > 25:
            newchar = newchar % 26
        shifted = chr(newchar+97)
        return shifted



def encrypt(text,rot):
    translatedText =""
    for i in text:
        translatedText+=(rotate_character(i,rot))
    return translatedText
