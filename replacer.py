#FREQUENCY ANALYSIS

file_name="frequency_rating.txt"

#read file line by line
try:
    with open(file_name) as f:
       content = f.read().splitlines()
except Exception:
    print ("Read error")
finally:
    f.close()

#replace characters according to their frequency
#to avoid extra letters replacements encr text is set to upper case and decr text  to lower
def replace(encrypted_text, ecnr_chars_rate=content):
    encrypted_text=encrypted_text.upper()
    for char in ecnr_chars_rate:
        decrypted_text=encrypted_text.replace(char.upper(), content[ecnr_chars_rate.index(char)].lower())
        encrypted_text=decrypted_text
    return decrypted_text

#test data
encr="bcabca"
rate=['b', 'c','a']
print (replace(encr,rate))
