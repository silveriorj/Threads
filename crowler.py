import urllib.request 
from bs4 import BeautifulSoup

url = "http://infopguaifpr.com.br"
html = str(urllib.request.urlopen(url).read())

sub = str(html).count("http://infopguaifpr.com.br/")
print("[INFO_FILHO] FILHAS: {}", format(sub))

soup = BeautifulSoup(html, 'html5lib')
links = soup.find_all("a")
tags = soup.find_all()

TAM_TAG = len(tags)
TAM_LINK = len(links)

print("\033[31m[INFO-PAI] Total de Tags encontradas : ", TAM_TAG)
print("[INFO-PAI] Total de Links encontrados: ", TAM_LINK, '\033[0;0m')

for link in links:
    tags = link.find_all()

   # print("[INFO] Link: ", links[i])