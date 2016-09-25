from dialog import *


# method 1 for numeric Polybius square cript
# and other methods for any text encripting
def get_list(cript, method=1):
    a = []
    if method==1:
        for i,v in enumerate(list(cript)):
            if i%2==0:
                a.append(v)
            else:
                a[-1] += v
    else:
        a = list(cript)
    return a

# cript must be a list from get_list method
# method returns list of tuples (unicode_letter, float_frequency) sorted by frequency
def get_freq(cript):
    l = list(set(cript))
    clen = len(cript)+.0
    freq_dic = {}
    for x in l:
        freq_dic[x]=0
    for x in cript:
        freq_dic[x] += 1
    for x in l:
        freq_dic[x] /= clen

    k = freq_dic.keys()
    v = [round(x,3) for x in freq_dic.values()]
    kv = zip(k,v)
    kv = sorted(kv,key=lambda x:(-x[1],x[0]))
    return kv

def get_real_freq(alphabet_file_name):
    import csv
    a = []
    with open(alphabet_file_name) as f:
        reader = csv.reader(f)
        for row in reader:
            #a.append((row[0].decode("utf8").upper(), float(row[1])))
            a.append((row[0].upper(), float(row[1])))
        return sorted(a,key=lambda x:(-x[1],x[0]))

def alphabet_freq(alphabet):
    if alphabet==1:
        afile = 'freq_tables/rus32.csv'
    elif alphabet==2:
        afile = 'freq_tables/rus37.csv'
    elif alphabet==3:
        afile = 'freq_tables/eng26.csv'
    else:
        afile = 'freq_tables/eng27.csv'
    return get_real_freq(afile)


def list_to_str(l):
    res = ''
    for i in l:
        res += i
    return res

def decrypt_(decr_type,crypt_,freq, real_freq):
    crypt = crypt_.copy()
    rep_stack=[]
    if decr_type == 2:
        i=0
        while len(freq)!=0:
            print('''input a symbol to replace {} or type:
"pr" to go to prev step
"re" to restart
"end" to exit'''.format(freq[i][0]))
            symb=input().lower()
            if symb=='end':
                return list_to_str(crypt)
            elif symb=='re':
                print_table_2(freq, real_freq)
                return decrypt_(decr_type,crypt_,freq, real_freq)
            elif symb=='pr':
                try:
                    crypt=replacer_by_yasha(crypt,rep_stack.pop())
                    i-=1
                except Exception:
                    print('Cannot move to previous step!')
            elif len(symb)==1:
                crypt = replacer_by_yasha(crypt, (freq[i][0],symb))
                rep_stack.append((symb,freq[i]  [0]))
                i+=1
            else:
                print('Enter one symbol!')
            print('now encryption is:\n{}'.format(list_to_str(crypt)))
    elif decr_type==1:
        for tup in freq:
            crypt=replacer_by_yasha(crypt,(tup[0], real_freq[freq.index(tup)][0].lower()))
    return list_to_str(crypt)

def replacer_by_yasha(l, tup_to_change):
    for i, v in enumerate(l):
        if v==tup_to_change[0]:
            l[i] = tup_to_change[1]
    return l
