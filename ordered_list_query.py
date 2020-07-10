from collections import defaultdict
import itertools
import operator
from itertools import product
import numpy as np

book_keeping = defaultdict()

def monotonically_increasing(lst):
    #https://stackoverflow.com/a/4983308
    pairs = zip(lst, lst[1:])
    return all(itertools.starmap(operator.le, pairs))

def list_products(product_list):
    if len(product_list) == 2:
        return product(book_keeping[product_list[0]],book_keeping[product_list[1]])
    else:
        return product(book_keeping[product_list[0]],list_products(product_list[1:]))
    
def ordered_list_search(query_lst,lst,book_keeping):
    #https://stackoverflow.com/a/6294744
    import numpy as np
    values = np.array(lst)
    search_value = query_lst[0]
    ii = np.where(values == search_value)[0]
    book_keeping[search_value] = list(ii)
    new_query_list = query_lst[1:]
    if new_query_list:
        ordered_list_search(new_query_list,lst,book_keeping)
    else:
        return 


ordered_list_search([3,4,5],[3,3,4,5,4,5],book_keeping)


results = []
for ix in list(list_products([3,4,5])):
    temp_lst = []
    for item in ix:
        #print(item,type(item))
        if isinstance(item,np.int64):
            temp_lst.append(item)
        if isinstance(item,tuple):
            for iy in item:
                temp_lst.append(iy)
    if monotonically_increasing(temp_lst):
        results.append(temp_lst)

results
#[[0, 2, 3], [0, 2, 5], [0, 4, 5], [1, 2, 3], [1, 2, 5], [1, 4, 5]]
