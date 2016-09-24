from logic import *
from dialog import *

crypt, variant, alphabet = input_dialog()
freq = get_freq(get_list(crypt, variant))
real_freq = alphabet_freq(alphabet)
decr_type=how_to_decrypt()
#print_table(freq,real_freq)
print_table_2(freq,real_freq)
decryption=decrypt_(decr_type,crypt,freq, real_freq)
print(decryption)
