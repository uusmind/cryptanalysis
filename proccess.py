from logic import *
from dialog import *

crypt, variant, alphabet = input_dialog()
freq = get_freq(get_list(crypt, variant))
real_freq = alphabet_freq(alphabet)