
import urllib
from bs4 import BeautifulSoup
import ssl
scontext = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
#url = raw_input('Enter - ')
url ='https://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Vinay.html'

def get_data(url,position,count,counter=0):
    #print counter, count
    while counter < count+1:
        counter +=1
        print 'retreiving url',url
        html = urllib.urlopen(url,context=scontext).read()
        soup = BeautifulSoup(html)
        tags = soup('a')
        url=re.findall('"(.*)"',str(tags[position-1]))[0]
        
        get_data(url,position,count,counter)
