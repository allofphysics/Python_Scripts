import requests
import re
import pandas as pd
from pandas import ExcelWriter
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_colwidth', -1)
import pandas as pd
from sqlalchemy import create_engine
disk_engine = create_engine('sqlite:///Races.db')


def _removeNonAscii(s): return "".join(i for i in s if ord(i)<128) #used to remove non ascii from column names

def save_xls(list_dfs, xls_path): #writes to excel file 
    writer = ExcelWriter(xls_path)
    for n, df in enumerate(list_dfs):
        df.to_excel(writer,'sheet%s' % n)
    writer.save()
#save_xls(df,xls_path)


#grabs all cheval urls
def horses_urls():
    horse_names_urls=[]
    for indx in xrange(26):
        letter=chr(97+indx)
        url='http://www.zone-turf.fr/cheval/lettre-{}.html'.format(letter)
        test=requests.get(url).content #grabs the html
        cheval_df=pd.read_html(test)  #reads html
        for url in re.findall('href="(/cheval/.{,25})/">',test):
            if url not in horse_names_urls:
                horse_names_urls.append(url+'/')
    return horse_names_urls

#grabs all jocky urls
def jockey_urls():
    jockey_names_urls=[]
    for indx in xrange(26):
        letter=chr(97+indx)
        url='http://www.zone-turf.fr/jockey/lettre-{}.html'.format(letter)
        test=requests.get(url).content
        cheval_df=pd.read_html(test)
        for url in re.findall('href="(/jockey/.{,25})/">',test):
            if url not in jockey_names_urls:
                jockey_names_urls.append(url+'/')
        return jockey_names_urls

def cheval_resume(name):

    max=0
    root_url='http://www.zone-turf.fr'+name+'resume-de-carriere/'
    testing=requests.get(root_url).content
    resume_df=pd.read_html(testing)
    
    
    resume_urls=re.findall('(archives.{,17})\'',testing)
    for archive in re.findall('archives.{1,10}',testing):
        numbers=re.split('\-|\.',archive)[1]
        if int(numbers)>max:
            max = int(numbers)

    for indx in range(1,max+1):
        url=root_url+'archives-{}.html?o=d&f=d'.format(indx)
        data=requests.get(url)
        resume_df[2]=resume_df[2].append(pd.read_html(url)[2])  #appending results to the dataframe
    
    
    return resume_df[2]
  
#cheval_resume('/cheval/atout-de-fontaine-249938/')

def jockey_resume(name):
    max=0
    root_url='http://www.zone-turf.fr/'+name
    testing=requests.get(root_url).content
    resume_df=pd.read_html(testing)
    resume_urls=re.findall('(archives.{,17})\'',testing)
    for archive in re.findall('archives.{1,10}',testing):
        numbers=re.split('\-|\.',archive)[1]
        if int(numbers)>max:
            max = int(numbers)
    max = min(max,10)
    print max
    for indx in range(1,max+1):
        url=root_url+'archives-{}.html?o=d&f=d'.format(indx)
        data=requests.get(url)
        resume_df[2]=resume_df[2].append(pd.read_html(url)[2]) #appending content
    return resume_df[2]
#jockey_resume('/jockey/a-jacob-68879/')

def race_scraper(base_url):
    content = requests.get(base_url).content
    df=pd.read_html(content)


    del df[5]
    del df[5]

    df[2].columns=[_removeNonAscii(i) for i in  df[2].columns.values] 

    tf=df[2]

    for indx in range(5,len(df[3:]),3):
        tf=tf.append(df[indx])




    tf.Cheval=tf.Cheval.str.replace('[A-Z]\d.*','')  #cleaning content
    tf.Cheval=tf.Cheval.str.lower().replace('\(SE\)','')
    tf.Cheval=tf.Cheval.str.replace('\s','_')
    tf.Cheval=tf.Cheval.str[:-1]
    tf=tf.reset_index()#resets the index 


    nan_list=tf.Driver[(tf.Driver=='NON PARTANTE')|(tf.Jockey=='NON PARTANT')|(tf.Driver=='NON PARTANT')|(tf.Jockey=='NON PARTANTE')].index.tolist()#deals with nan values in driver and jockey 
    print nan_list
    jockey_url_list=re.findall('href="(/jockey/.{,50}/)"',content)
    print len(jockey_url_list)
    for indx in nan_list:
        jockey_url_list.insert(indx,'NaN')        
    print len(tf)
    #print len(jockey_url_list)
    #print jockey_url_list
    tf['jockey_Url']=jockey_url_list
    cheval_urls=re.findall('href="(/cheval/.{,90}/)',content)
    tf['cheval_urls']=[url for url in cheval_urls if '</strong>' not in url]
    tf=tf.fillna('')
    ########################################################################################
    df[1].to_excel('Race_Info.xls')
    df[1].columns=[_removeNonAscii(i) for i in  df[1].columns.values] 
    df[1].to_sql('race_info', disk_engine, if_exists='replace')



    tf.to_excel('Races5.xls')

    cheval_url_list=[]
    #tf=tf.reset_index()
    tf.columns=[_removeNonAscii(i) for i in  tf.columns.values] 
    tf.to_sql('races', disk_engine, if_exists='replace') 


    for indx in tf.index:
        url=tf.cheval_urls.ix[indx]
        cheval_url_list.append(url)
        #table_name=re.sub('/cheval/|/|\-','',url)
        print url
        #print url
        #cheval_resume_df_lst.append(cheval_resume(url))
        #cheval_resume_df_lst[indx].to_sql(table_name, disk_engine, if_exists='replace')
        try:
            if cheval_url_list.count(url)==1:
                cheval_resume(url).to_sql('chevals', disk_engine, if_exists='append') #writes data to table
            else:
                print 'duplicate'
        except:
            print url+'FAILED###############'
    #save_xls(cheval_resume_df_lst,'Chevals_Resumes.xls')

    jockey_url_list=[]
    for indx in tf.index:

        url=tf.jockey_Url.ix[indx]
        jockey_url_list.append(url)
        print url
        #table_name=re.sub('/jockey/|/|\-','',url)
        #jockey_resume_df_lst.append(jockey_resume(url))
        #jockey_resume_df_lst[indx].to_sql(table_name, disk_engine, if_exists='replace')
        try:
            if jockey_url_list.count(url)==1:
                jockey_resume(url).to_sql('jockey', disk_engine, if_exists='append') #writes data to tables
            else:
                print 'duplicate'
        except:
            print url+'FAILED###############'







#### Grabs the main pages ####################################################
race_list=[]
content = requests.get('http://www.zone-turf.fr/programmes/').content
for race in re.findall('/programmes.{,50}html',content):
    if race not in race_list:
        race_list.append('http://www.zone-turf.fr'+race)

for race in race_list:
    try:
        base_url=race
        race_scraper(base_url)
    except:
        print 'errors in scraping ',race
