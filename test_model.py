
from models.newspaper.newspaper import Article
# url = ""
url = 'https://www.onlinekhabar.com/2019/05/765579'
lang = "ne"
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



