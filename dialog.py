def input_dialog():
    print ('''input name of file with encrypted text like this: "name.txt"
    otherwise 'encrypted.txt' file would be used''')
    file_name = input()

#    print ('''\nchoose your variant of input:
#1. message encrypted with a Polybius square (by digits)
#2. message encrypted with a symbolic alphabet''')
#    variant = int(input())

    variant=input_variant()

    alphabet = input_alphabet()

    try:
        f = open(file_name)
    except Exception:
        f=open('encrypted.txt')

    #crypt = f.read().decode("utf8").upper().replace('\n','')
    crypt = f.read().upper().replace('\n','')
    print ('your message is:')
    print ('-'*len(crypt))
    print (crypt)
    print ('-'*len(crypt))
    return ([crypt, variant, alphabet])

def print_table(freq, real_freq):
    for tup in freq:
        print('{0} --  {1}'.format(tup[0], real_freq[freq.index(tup)][0]))

def input_variant():
    print ('''\nchoose your variant of input:
1. message encrypted with a Polybius square (by digits)
2. message encrypted with a symbolic alphabet''')
    while True:
        variant=input()
        try:
            return int(variant)
        except Exception:
            print('input number')


def input_alphabet():
    print (u'''\nchoose alphabet of decrypted text:
   cyrillic
1. cyrillic without seperators <- 32 chars
2. cyrillic with seperators    <- 37 chars (currently unavailable)
   latin
3. A|B|C|...|Z    <- 26 chars
4. A|B|...|Z|_    <- 27 chars''')
    while True:
        variant=input()
        try:
            return int(variant)
        except Exception:
            print('input number')

def how_to_decrypt():
    print('''choose how to swap letters:
1. replace all letters at once according to theoretical frequency table
2. replace letters one by one''')
    while True:
        variant=input()
        try:
            return int(variant)
        except Exception:
            print('input number')
