# -*- coding: utf-8 -*-

import ssl,requests
from bs4 import BeautifulSoup
x=raw_input("Search : ")
r = requests.get("http://en.wikipedia.org/w/index.php?search="+x+"&title=Special%3ASearch&go=Go")
html=r.content
bsObj = BeautifulSoup(html,"html.parser")
bsObj = bsObj.select('#mw-content-text > p')
for link in bsObj:
    m=link.get_text()
    for i in range(1,20):
        m=m.replace('['+str(i)+']','')
    print m.encode("utf")
    
