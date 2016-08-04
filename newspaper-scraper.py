# -*- coding: utf-8 -*-
from urllib2 import urlopen
from bs4 import BeautifulSoup
dash='--------------------------------------------------------------------------------------'
x=raw_input('ENTER NEWSPAPER NAME [ TOI | TS | TH ] :\t\t\t')
x=x.strip()
x=x.upper()
nw=' NEWS'
lnh='LATEST'
sn='SPORTS'
ent='ENTERTAINMENT'
biz='BUSINESS'
ls='LIFE STYLE'
wd='WORLD'
st='SCIENCE & TECHNOLOGY'
y=int(raw_input('ENTER CODE [ 1. '+lnh+' | 2. '+sn+' | 3. '+ent+' | 4. '+ls+' | 5. '+biz+' | 6. '+wd+' | 7. '+st+' ] :\t'))
if x=='TOI':
    url='timesofindia.indiatimes'
    a='\n\n'
    b=''
    if y==1:
        param=".list9"
    elif y==2:
        param='[data-vr-zone~=sports] > li'
    elif y==3:
        param='[data-vr-zone~=ots] > li'
    elif y==4:
        param='#life-&-stylewidget > ul.list2 > li'
    elif y==5:
        param='[data-vr-zone~=business] > li'
    elif y==6:
        param='[data-vr-zone~=world] > li'
    elif y==7:
        param='[data-vr-zone~=science] > li'
elif x=='TS':
    url='thestatesman'
    a=''
    b=''
    if y==1:
        param='a[href^="/news/latest-headlines/"]'
    elif y==2:
        param='.menuItems ul:nth-of-type(3) li a'
    elif y==3:
        param='.menuItems ul:nth-of-type(12) li a'
    elif y==4:
        param='.menuItems ul:nth-of-type(10) li a'
    elif y==5:
        param='.menuItems ul:nth-of-type(4) li a'
    elif y==6:
        param='.menuItems ul:nth-of-type(2) li a'
    elif y==7:
        param='a[href^="/news/science-and-tech/"]'
elif x=='TH':
    url='thehindu'
    a=''
    b=''
    if y==1:
        param="#opanel1 > div > h4 > a"
    elif y==2:
        param='[data-vr-zone~=Sport] > div > [class~=one-fourthcolumn] > div > a'
    elif y==3:
        param='[data-vr-zone~=Entertainment] > div > [class~=one-fourthcolumn] > div > a'
    elif y==4:
        param='[data-section-name~=Magazine] > div > h3 > a'
    elif y==5:
        param='[data-vr-zone~=Business] > div:nth-of-type(2) > div.border-btm > a'
    elif y==6:
        param='[data-vr-zone~=International] > div:nth-of-type(2) > div.border-btm > a'
    elif y==7:
        param='#ggtcon660 > div > div > h3 > a'
html = urlopen("http://www."+url+".com/")
bsObj = BeautifulSoup(html,"html.parser")
bsObj = bsObj.select(param)
if y==1:
    header=lnh
elif y==2:
    header=sn
elif y==3:
    header=ent
elif y==4:
    header=ls
elif y==5:
    header=biz
elif y==6:
    header=wd
elif y==7:
    header=st
print('\n'+header+nw+'\n'+dash);
i=0
for link in bsObj:
    if x=='TS' and i%2==0:
        i+=1 
        continue
    else:
        i+=1
        text=link.get_text()
        sep = 'Adv:'
        rest = text.split(sep, 1)[0]
        rest=rest.replace(a,b)
        rest=rest.rstrip()
        print rest.encode('utf')
print dash
