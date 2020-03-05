import pandas as pd
pd.options.display.max_rows = 999
f =open('some_file.py')
data = f.read()
f.close()

lst = [ord(x) for x in data]
chars = set(lst)

dct = {}
for char in chars:
    dct[char] = lst.count(char)

def ngram_lst(n):
    for ix,char in enumerate(lst):
        if ix != len(lst)-(n-1) and n !=1:
            if tuple([chr(x) for x in lst[ix:ix+n]]) not in dct.keys():
                dct[tuple([chr(x) for x in lst[ix:ix+n]])] = 1
            else:
                dct[tuple([chr(x) for x in lst[ix:ix+n]])] += 1

for ix in range(2,500):
    ngram_lst(ix)

df = pd.DataFrame(pd.Series(dct))
df = df.sort_values(0,ascending=False)
df.reset_index(inplace=True)
df =df[df[0] >1]
df =df[df['index'].apply(lambda x: '(' in str(x))]
df = df.sort_values(['index',0])
df.to_csv('test.csv')
