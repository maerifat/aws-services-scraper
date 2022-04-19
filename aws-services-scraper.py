import requests
from bs4 import BeautifulSoup as bs
import html5lib

url ="https://awscli.amazonaws.com/v2/documentation/api/latest/reference/index.html"

r= requests.get(url)
content= r.content

soup = bs(content, 'html.parser')

setx =[]
finallist=[]
ultilist=[]

baseurl="https://awscli.amazonaws.com/v2/documentation/api/latest/reference/"


for link in soup.find_all("a", class_="reference internal"):
    endpoint= link.get('href')
    if ".html" in endpoint:
        finallink = baseurl+endpoint
        finallist.append(finallink)
        
        url2 = finallink
        r2 =requests.get(url2)
        content2 = r2.content
        soup2 = bs(content2, 'html.parser')
        for link2 in soup2.find_all("a", class_="reference internal"):
            endpoint2= link2.get('href')
            finallink2 = finallink.replace("index.html", endpoint2)
            ultilist.append(finallink2)
            print(finallink2)
            if "#" not in finallink2:
                try:
                    linksfile = open("servicelinksfile.txt", "a")
                    linksfile.write(finallink2+"\n")
                    linksfile.close()
                except:
                    print("something went wrong. please make sure you have sufficient permissions to create a file.")
            
            
print("Task Completed. Data has been saved inside servicelinksfile.txt")
