import re

f=open('modeler_jobs.log','r')
data=f.readlines()
g=open('out.log','w')
for line in data:
	resp=re.split('(\s\-\w+\s)', line)
	d={"command":resp[0].split(' ')[0].replace('$',''),'timestamp':resp[0].split(' ')[-1].replace('{','').replace('}','').replace('\n','')}
	d.update({x:y for (x,y) in zip (resp[1::2],resp[2::2])})
	g.write(str(d))
