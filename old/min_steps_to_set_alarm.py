def alarmClock(setTime, timeToSet):
    seta,setb=setTime.split(':')
    ta,tb=timeToSet.split(':')
    print min((int(seta)-int(ta))%24,(int(ta)-int(seta))%24)+min(abs((int(setb)-int(tb))%60),(int(tb)-int(setb))%60)
    
print alarmClock("07:30", "08:00")  #output 31
