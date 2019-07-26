import bs4 as bs
import urllib.request
from utils import summarizer

scraped_data = urllib.request.urlopen('https://en.wikipedia.org/wiki/Artificial_intelligence')
article = scraped_data.read()

parsed_article = bs.BeautifulSoup(article,'lxml')

paragraphs = parsed_article.find_all('p')

article_text = []

for p in paragraphs:
	if len(p) > 1:
		article_text.append(p.text)
		#print (p.text.encode("utf-8"))
		#print(len(p.text))

for para in article_text:
	print(summarizer(para,2).encode("utf-8"))