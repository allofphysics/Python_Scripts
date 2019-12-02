def largest_substring_match(string1,string2):
    match=''
    lst=[]
    for indx,letter in enumerate(string1):
        match+=letter
        if match in string2:
            lst.append(match)
        else:
            lst.append('')
            match=''
    return max(lst,key=len)
