import requests
data=requests.get('').content #needs a url
def get_urls(data):
    urls=[]
    for line in data.split('\n'):
        resp=re.findall('href.*?(?:>|$|\s)',str(line),re.DOTALL)
        if len(resp)>0:
            for url in resp:
                url=re.sub('.*\.(png|xml)|javascript:void\(0\);','',url)
                url=re.sub('#','/',url)
                urls.append(re.sub('href=|\'|"|>','',url))
    return urls
