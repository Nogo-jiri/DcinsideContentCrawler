import requests
from bs4 import BeautifulSoup

url=input("게시글 URL을 입력하세요: ")

headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'}

resp=requests.get(url,headers=headers)

soup=BeautifulSoup(resp.content,'html.parser')

title=soup.select('.title_subject')[0].text

print(title)

#for anchor in contents:
#    print(anchor.find('span.title_subject'))

'''
for i in contents:
    print('-'*15)
    title_tag=i.find('a')
    title=title_tag.text
    print("제목: ",title)
'''
