from logic import *
from dialog import *
try:
    crypt, variant, alphabet = input_dialog()
    freq = get_freq(get_list(crypt, variant))
    real_freq = alphabet_freq(alphabet)
    decr_type=how_to_decrypt()
    print_table_2(freq,real_freq)
    decryption=decrypt_(decr_type,get_list(crypt,variant),freq, real_freq)
    print(decryption)
except Exception:
    print('Oops, something went wrong.Probably you chose wrong encryption or alphabet. Try again')
