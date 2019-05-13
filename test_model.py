
from models.newspaper.newspaper import Article
# url = ""
url = 'http://fox13now.com/2013/12/30/new-year-new-laws-obamacare-pot-guns-and-drones/'
lang = "en"
article = Article(url, language=lang)
article.download()
article.parse()
article.nlp()
data ={
		"TITLE": article.title,
		"keywords": article.keywords,
		"summary" :article.summary,
		"TEXT" : article.text,
		"img_url": article.top_image,
	}
print (data)



