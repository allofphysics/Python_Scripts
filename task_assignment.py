
def tasksScheduling(workingHours, tasks):
    if max(tasks)>workingHours:
        return -1
    a=tasks.count(workingHours)
    for ix in range(a):
        tasks.remove(workingHours)
    
    if tasks==[]:
        return a
    if len(tasks)==1:
        return 1
    tasks=sorted(tasks)
    count =0 
    while len(tasks)>1:
        if tasks[-1]+tasks[0]<workingHours:
            tasks[-1]+=tasks[0]
            
            del tasks[0]
        elif tasks[-1]+tasks[0]==workingHours:
            count+=1
            del tasks[0]
            del tasks[-1]
        elif tasks[-1]+tasks[0]>workingHours:
            del tasks[-1]
            count +=1
    return count+a+len(tasks)
tasksScheduling(7,[1, 4, 1, 1, 4, 4])
