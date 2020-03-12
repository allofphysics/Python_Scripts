import pandas as pd
from sys import argv
import pickle
from os import listdir 

index_exists = [x for x in listdir('.') if 'index' == str(x)]
if index_exists:
    try:
        f = open('index','rb')
        index = pickle.loads(f.read())
        f.close()
    except Exception as e:
        print(e)
else:
    index = {}


ngrams_count_exists = [x for x in listdir('.') if 'ngrams_count' == str(x)]
if ngrams_count_exists:
    try:
        f = open('ngrams_count','rb')
        ngrams_count = pickle.loads(f.read())
        f.close()
    except Exception as e:
        print(e)
else:
    ngrams_count = {}
 



f =open(argv[1])
data = f.read()
f.close()

from random import randint
lst = [ord(x) for x in data]

from tqdm import tqdm
ngrams = []
for i in tqdm(range(1,10)):
    for ix,xs in enumerate(lst[:-i]):
        ngram = tuple(lst[ix:ix+i])
        ngrams.append(ngram)
        if ngram not in index.keys():
            index[ngram]= len(index)


s = set(ngrams)
for ix in s:
    count = ngrams.count(ix)
    if ix not in ngrams_count.keys():
        ngrams_count[ix] = count
    else:
        ngrams_count[ix] += count




serialized_index = pickle.dumps(index)
with open('index','wb') as f:
    f.write(serialized_index)
f.close()

serialized_ngrams_count = pickle.dumps(ngrams_count)
with open('ngrams_count','wb') as f:
    f.write(serialized_ngrams_count)
f.close()


print(len(index))
dct = sorted(ngrams_count.items(),key=lambda  x:-x[1])
import  pandas as pd
df  = pd.DataFrame(dct)
print(df.to_csv('text.csv'))
























