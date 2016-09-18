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
            a.append((row[0].decode("utf8").upper(), float(row[1])))
        return sorted(a,key=lambda x:(-x[1],x[0]))
    
def alphabet_freq(alphabet):
    if alphabet==1:
        afile = 'rus32.csv'
    elif alphabet==2:
        afile = 'rus37.csv'
    elif alphabet==3:
        afile = 'eng26.csv'
    else:
        afile = 'eng27.csv'
    return get_real_freq(afile)