"""
The goal is to learn how to work with nested dictionaries

(
{1: {2: {3: 5}}}, 
{1: {2: {4: 4}}
) => {1: {2: {3: 5, 4: 4}}}

"""
def pack(lst):
    if isinstance(lst, list):
        if len(lst) > 1:
            return {lst[0]: pack(lst[1:])}
        else:
            return lst[0]
    if isinstance(lst, dict):
        return lst
    else:
        if isinstance(lst, list):
            return {lst[0]}


master = pack([1, 2, 3, 5])
child = pack([1, 2, 4, 4])
print(master,child)

master_temp_dict = master.copy()
child_temp_dict = child.copy()
temp_keys = []


def shared_key(master, child):
    try:
        if isinstance(child, dict):
            if list(child.keys())[0] in list(master.keys()):
                key = list(child.keys())[0]
                temp_keys.append(key)
                master = master.get(key)
                child = child.get(key)
                return shared_key(master, child)
            else:
                master.update(child)
                temp_keys.append(master)
                return pack(temp_keys)
        else:
                master.update(child)
                temp_keys.append(master)
                return pack(temp_keys)

    except:
        pass
        #from pudb import set_trace
        # set_trace()


x = shared_key(master, child)
print(x)
