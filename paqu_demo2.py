
import re
import requests
import sys
import  time
reload(sys)
sys.setdefaultencoding('utf-8')
songID=[]
songName=[]
for i in range(0,2):
    url="http://www.htqyy.com/top/musicList/hot?pageIndex="+str(i)+"&pageSize=20"

    html=requests.get(url)
    aa=html.text

    pat1=r'title="(.*?)" sid'
    pat2=r'sid="(.*?)"'
    idlist=re.findall(pat2,aa)
    titlelist=re.findall(pat1,aa)
    songID.extend(idlist)
    songName.extend(titlelist)

for i in range(0,len(songID)):
    songUrl="http://f2.htqyy.com/play7/"+str(songID[i])+"/mp3/3"
    songname=songName[i]
    data=requests.get(songUrl).content
    print(i+1)
    with open("E:\\music\\{}.mp3".format(i),"wb") as f:
        f.write(data)