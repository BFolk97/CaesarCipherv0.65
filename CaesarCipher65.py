# Caesar Cipher v 0.62
# Ben Folk
# 7 January 2019

from datetime import datetime

g = open('cipherText.txt', 'a') # Makes a file for your ciphers.

list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'] # Alphabet
otherlist = [] # List to hold final string
cont = 'y' # Important tick marker in the while loop

print('Caesar Cipher v 0.65\nAvailable for all of your ciphering needs.\nFollow the onscreen instructions please.\n\n')

while cont.lower() == 'y' or cont.lower() == 'yes': 
    sentence = str(input('Enter string to be scrambled:\n'))
    count = 1
    while count != 0:
        try:
            modifier = int(input('What value do you want to modify the cipher by:\n       (Between +26 and -52, inclusive)\n\n'))
            if modifier > 26 or modifier < -52: #Values above positive 26 and or below negative 52 lead to index errors, as the code only makes 
                print('Please select a number between +26 and -52')
                continue
            count = 0
        except ValueError:
            print('This needs to be a number between -52 and 26.')
            continue
    e = sentence.lower() 
    f = [c for c in e] # Makes a list of every individual character in the 'sentence' varaible, which is then iterated over in the for loop.
    for i in f:
        if i not in list: # Appends non-lexical characters, like number punctuation and so on 
            otherlist.append(i)
            continue
        else: # Swaps letter for another letter in the alphabet, based on the 'modifier' number.
            i.find(e) in list
            letVal = list.index(i)
            letValNew = letVal + modifier
            if letValNew > 25: # Catches overflows when letters go beyond 'z'. * 
                letValOther = letValNew - 26
                new = list[letValOther]
            elif letValNew < 0: # Catches overflows when letters go beyond 'a'. *
                letValOther = letValNew + 26
                new = list[letValOther]
            else:
                new = list[letValNew]
            otherlist.append(new)
        a = ''.join(otherlist)
        
    now = datetime.now()
    x = '| Creation Date : ', str(now), '\n', '| Modifier Value : ', str(modifier), '\n', '| Encryption : ', str(a), '\n', '|', '\n'
    y = ''.join(x)
    print('\nEncrypted message : ', a, '\n') # Just shows output
    g.write(y) # Appends all of the key information from the cipher onto a notepad for later viewing, if one wishes to do so.
    otherlist = [] # Clears the list for repeat entries
    cont = str(input('Would you like to generate a new word?\nType "y" or "yes" to continue; hit any other key to exit.\n'))

g.close()
print('Operations concluded...')