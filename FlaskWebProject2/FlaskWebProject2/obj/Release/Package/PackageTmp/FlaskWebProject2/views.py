"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template,request
from FlaskWebProject2 import app
import requests

@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/contact')
def contact():
    """Renders the contact page."""
    return render_template(
        'contact.html',
        title='Contact',
        year=datetime.now().year,
        message='Your contact page.'
    )

@app.route('/about')
def about():
    """Renders the about page."""
    return render_template(
        'about.html',
        title='About',
        year=datetime.now().year,
        message='Your application description page.'
    )
@app.route('/flipkart',methods=['GET'])
def flipkart():
    #url = url.replace('|','/')
    #url = url.replace(';','?')
    url = request.args.get('url')
    r = requests.get(url)
    final = r.content.decode("utf-8")
    search="selling-price omniture-field"
    a=final.find(search)
    b=final.find(">",a)
    a=final.find("<",b)
    return final[b+1:a]

@app.route('/snapdeal',methods=['GET'])
def snapdeal():
    #url = url.replace('|','/')
    #url = url.replace(';','?')
    url = request.args.get('url')
    r = requests.get(url)
    final = r.content.decode("utf-8")
    search="payBlkBig"
    a=final.find(search)
    b=final.find(">",a)
    a=final.find("<",b)
    return final[b+1:a]


@app.route('/amazon',methods=['GET'])
def amazon():
    #url = url.replace('|','/')
    #url = url.replace(';','?')
    url = request.args.get('url')
    r = requests.get(url)
    final = r.content.decode("utf-8")
    search="priceblock_saleprice"
    a=final.find(search)
    if(a==-1):
         search="priceblock_ourprice"
         a=final.find(search)
    b=final.find(">",a)
    a=final.find(">",b+1)
    b=final.find(">",a+1)
    a=final.find(">",b+1)
    b=final.find(">",a+1)
    a=final.find(">",b+1)
    b=final.find(">",a+1)
    a=final.find("<",b+1)
    #b=final.find(">",a+1)
    #a=final.find(">",b+1)

    #b=final.find("",a)
    lol=final[b+1:a]
    return lol


