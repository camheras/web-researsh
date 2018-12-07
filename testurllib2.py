import urllib.request as urllib
from urllib.request import Request, urlopen
import re

url = "http://google.com/"

def get(request):
    res = Request('https://duckduckgo.com/?q='+str(request)+'&t=h_&ia=news', headers={'User-Agent': 'Mozilla/5.0'})
    res = urlopen(res).read()

    links = re.findall('"((http|ftp)s?://.*?)"', str(res))
    print(links)

get("test")
