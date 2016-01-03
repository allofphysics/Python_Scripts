def fileNaming(names):
    renames=[x for x in names if names.count(x)>1]
    for item in set(renames):
        indices = [i for i, x in enumerate(names) if x == item]
    for ix,test in enumerate(indices[1:]):
        if names[test]+'('+str(ix+1)+")" not in names[:ix]:
            
            names[test]=names[test]+'('+str(ix+1)+")"
        else:
            names[test]=names[test]+'('+str(ix+2)+")"
    if len(set(names)) == len(names):
        return names
    else:
        return fileNaming(names)
