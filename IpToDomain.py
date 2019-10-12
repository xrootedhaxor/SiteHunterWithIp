#Author: https://github.com/CrypticWizard
import requests 
from bs4 import BeautifulSoup
def IpToDomain(): 
	print("Started  For Collecting Site...")
	f=open('ip.txt', 'r').read().split('\n') 
	with open('result.txt', 'w') as result:
		for line in f:
			if line == "":
				continue;
			ips=line.split(".")
			ipc= ips[0]+"."+ips[1]+"."+ips[2]+"."
			for i in range(0,256):
				ipm=ipc+str(i)
				ip=str(ipm)
				result.write("ip:"+ip+"\n")
IpToDomain() 
def BingBot():
	headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'}
	url1= 'https://www.bing.com/search?q='
	o=open("result.txt", 'r').read().split("\n")
	for line in o:
		search=str(line)
		if search=="":
			continue;
		url=url1+search 
		req= requests.get(url, headers=headers)
		r=req.text
		soup = BeautifulSoup(r, 'html.parser')
		re=soup.find("ol", {"id": "b_results"})
		l=re.findAll("li", {"class": "b_algo"}) 
		links=[]
		for item in l:
			try:
				href=item.find("a").attrs["href"]
				links.append(href)
			except:
				pass
		for l in links:
			open('links.txt', 'a+').close()
			l=l.split('/')
			l=l[0]+'//'+l[1]+l[2]
			if l not in open('links.txt', 'r').read():
				open('links.txt', 'a+').write(l+'\n')
				print(l)
print("Site Collection Finished")
BingBot() 

	
	
			
		
	
	
