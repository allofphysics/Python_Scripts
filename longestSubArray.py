def findSubArrayWithSameElement(a, k):
    ans=''
    try:
        temp=[ix for ix,x in enumerate(a) if x == k]
        lst=temp
        min=lst[0]
        max=0
        newlst=[]
        for x in range(len(lst)-1):
            if lst[x+1]==lst[x]+1:
                max=lst[x+1]
            else:

                newlst.append((min,max,max-min))
                min=lst[x+1]
        newlst.append((min,max,max-min))
        ans=list(sorted(newlst,key=lambda x: x[2])[-1][0:2])
    except:
        pass
    if len(ans)==0:
        return [-1,-1]
    else:
        return ans
