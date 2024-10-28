def ceaser_encrypt(text,shift):
    etext=""
    for i in range(len(text)):
        char=text[i]
        if char==" ":
            etext+=" "
            continue;
        if char.isupper():
            etext+= chr((ord(char)+shift -65)%26 + 65);
        else:
            etext+= chr((ord(char)+shift -97) % 26 +97);
    return etext

def ceaser_decrypt(etext,shift):
    dtext=""
    for i in range(len(etext)):
        char=etext[i]
        if char==" ":
            dtext+=" "
            continue;
        if char.isupper():
            dtext+= chr((ord(char)-shift -65)%26 + 65);
        else:
            dtext+= chr((ord(char)-shift -97) % 26 +97);
    return dtext
text='Hello World'
entext=ceaser_encrypt(text,3)

detext=ceaser_decrypt(entext,3)

print(entext, detext)