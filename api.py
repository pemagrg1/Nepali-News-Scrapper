from flask import Flask, request, render_template,jsonify
from models.newspaper.newspaper import Article
# from models.newspaper.newspaper import fulltext
import json


app = Flask(__name__)
app.debug = True


@app.route('/')
def load_home():
    return render_template("home.html")


"""
For Php API
"""
@app.route('/analyse', methods=['POST','GET'])
def analyse():
    data = request.data.decode("utf-8")
    data = json.loads(data)
    if not verify_token(data["token"]):
        return ('token did not matched')

    # data = request.form.to_dict()
    url = data["url"]
    print (url)
    article = Article(url, language='hi')
    article.download()
    article.parse()
    article.nlp()

    data_to_send = {
        "DATE": article.publish_date,
        "TITLE": article.title,
        "keywords": article.keywords,
        "summary" :article.summary,
        "TEXT" : article.text,
        "img_url": article.top_image,
        "video" : article.movies,
        "url":url,
    }
    result = {str(key): value for key, value in data_to_send.items()}
    return jsonify(result=data_to_send)


"""
For Web API
"""
@app.route('/analyse_web', methods=['POST','GET'])
def analyse_web():
    data = request.form.to_dict()
    # data = request.form.to_dict()
    url = data["url"]
    print (url)
    article = Article(url, language='hi')
    article.download()
    article.parse()
    article.nlp()

    data_to_send = {
        "DATE": article.publish_date,
        "TITLE": article.title,
        "keywords": article.keywords,
        "summary" :article.summary,
        "TEXT" : article.text,
        "img_url": article.top_image,
        "video" : article.movies,
        "url":url,
    }
    print (data_to_send)
    result = {str(key): value for key, value in data_to_send.items()}
    return jsonify(result=data_to_send)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=11706)
