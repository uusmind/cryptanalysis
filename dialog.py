def input_dialog():
    print '''input name of file with encrypted text like this: "name.txt"
    otherwise 'encrypted.txt' file would be used'''
    file_name = input()

    print '''\nchoose your variant of input:
1. message encrypted with a Polybius square (by digits)
2. message encrypted with a symbolic alphabet'''
    variant = int(input())
    
    print u'''\nchoose alphabet of decrypted text:
   cyrillic
1. cyrillic without seperators <- 32 chars
2. cyrillic with seperators    <- 37 chars
   latin
3. A|B|C|...|Z    <- 26 chars
4. A|B|...|Z|_    <- 27 chars'''
    alphabet = int(input())

    f = open(file_name)
    crypt = f.read().decode("utf8").upper().replace('\n','')
    print 'your message is:'
    print '-'*len(crypt)
    print crypt
    print '-'*len(crypt)
    return [crypt, variant, alphabet]
