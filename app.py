import pymongo
from flask import Flask, render_template, redirect
import scrape_mars

app = Flask (__name__)

client = pyMongo.MongoClient()
db = client.mars_page_db
collection = db.mars_all

@app.route('/scrape')

def scrape ():
    mars = scrape_mars
    return(mars)

@app.route('/')

def home ():
    mars_= db.mars_all
    return render_template ('index.html', mars= mars)

if __name__ == "__main__":
    app.run(debug=True)
