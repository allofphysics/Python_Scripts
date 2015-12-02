
# coding: utf-8

# In[14]:

import pandas as pd
import numpy as np
from datetime import datetime
import datetime
from pandas import read_table
pd.set_option('display.max_rows',500)
pd.set_option('display.width',1000)
import subprocess
from redis import Redis
redis_client=Redis(host='127.0.0.1', port=6379, db = 3)

#def runShellCmd(cmd):
#    run = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
#    out, err = run.communicate()
#    if err:
#        print err

#if you have w3m install this will pull the page from the site
#cmd='w3m  http://www.sanfoundry.com/python-quiz-online/ >test2.txt'
#runShellCmd(cmd)


name_of_quiz = 'strings1.txt'
df=pd.read_table('test2.txt',names=['a'])
start=df.a[df.a.str.contains('1\.')].index.tolist()[0]
end=df.a[df.a.str.contains('Sanfoundry Global Education')].index.tolist()[0]
df=df[start:end]
df.replace('View Answer','',inplace=True)
questions_index_list=df[df.a.str.contains('^\d{1,}\..*\?')].index.tolist()
explanation_index=df[df.a.str.contains('Explanation')].index.tolist()
answer_index=df.a[df.a.str.contains('Answer')].index.tolist()

def prob_fun(start,stop,score):
    
    test=pd.Series(questions_index_list)
    problem=df.a.ix[test[start]:test[stop]-1]
    ans_index=(problem[problem.str.contains('Answer')].index.tolist())[0]
    for line in problem.ix[:ans_index-1]:
        print line
    test=raw_input()
    real_ans=df.ix[ans_index][0].split(':')[1].strip()
    if test==real_ans:
        print('Correct')
        score += 1
    else:
        print("Not Correct")
        score = score
        print('\n')
        for indx in problem.ix[ans_index:]:
            print (indx)
        
    return score






score = 0
counter = 0
scoring = {}

for ix in  range(len(questions_index_list)-1):
    start = datetime.datetime.now()
    score=prob_fun(ix,ix+1,score)
    finish = datetime.datetime.now()
    time_taken = finish - start
    print score
    counter += 1
    scoring[counter]=time_taken
percentage=float(score)/counter


time=datetime.datetime.now()
redis_client.hmset(name_of_quiz,{time:percentage*100})
redis_client.hmset(name_of_quiz,scoring)




