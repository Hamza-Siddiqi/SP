import requests
from bs4 import BeautifulSoup

def searchKeywords(Article_URL, keywords):
	if Article_URL!="":
		try:
			status=requests.get(Article_URL)
			if status.status_code==200:
				parser_object=BeautifulSoup(status.content,"html.parser")
				div_tags=parser_object.find_all('div',{'class':'the-post-content'})
				for div in div_tags:
					p_tags=div.find_all('p')
					for p in p_tags:
						for word in keywords:
							if word in p.text:
								return True
		except requests.ConnectionError:
			print "Error! Connection could not be established."
	return False

def getArticle(Sports_URL):
	if Sports_URL!="":
		try:
			count=0
			keywords=[]
			URL_list=[]
			choice="Y"
			status=requests.get(Sports_URL)
			
			if status.status_code==200:
				print "Connection Established!"
				print "Give some keywords to search."
				while choice=="Y" or choice=="y":
					string=raw_input("Enter a keyword : ")
					keywords.append(string)
					choice=raw_input("Continue (Y) Exit (N) : ")
					while choice!='Y' and choice!='y' and choice!='N' and choice!='n':
						choice=raw_input("Continue (Y) Exit (N) : ")

				parser_object=BeautifulSoup(status.content,"html.parser")
				article_tags=parser_object.find_all('article')
				for article in article_tags:
					if count==5:
						break
					header_tags=article.find_all('header')
					for header in header_tags:
						a_tags=header.find_all('a')
						for a in a_tags:
							keyword_found=searchKeywords(a['href'], keywords)
							if keyword_found==True:
								URL_list.append(a['href'])

					count+=1
				return URL_list
		except requests.ConnectionError:
			print "Error! Connection could not be established."

def getSports(URL):
	if URL!="":
		try:
			URL_list=[]
			status=requests.get(URL)

			if status.status_code==200:
				parser_object=BeautifulSoup(status.content,"html.parser")
				li_tags=parser_object.find_all('li',{'class':'menu-item menu-item-type-taxonomy menu-item-object-category nav-item menu-item-173920'})
				for li in li_tags:
					a_tags=li.find_all('a')
					for a in a_tags:
						URL_list=getArticle(a['href'])
				return URL_list
		except requests.ConnectionError:
			print "Error! Connection could not be established."

def main():
	URL="https://propakistani.pk/"
	URL_list=getSports(URL)
	print "The keywords were found in the following URL's : "
	for URL in URL_list:
		print URL

if __name__ == "__main__":
	main()
