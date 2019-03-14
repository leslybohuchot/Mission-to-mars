from bs4 import BeautifulSoup as bs
import pymongo
import pandas as pd
from splinter import Browser
import requests

def browser_start():
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    browser = Browser('chrome', **executable_path, headless = False)
    url = "https://mars.nasa.gov/news/?     page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"

    browser.visit(url)

    html = browser.html

    response = requests.get(url)
    soup = bs(html, 'html.parser')

    return(soup.prettify())


def scrape_mars():

    title = soup.title.text
    print(title)
    news_title = soup.find('div', class_= 'content_title').find('a').text
    news_p = soup.find('div', class_ = 'article_teaser_body').text
    image_url = 'https://www.jpl.nasa.gov/spaceimages/images/largesize/PIA16225_hires.jpg'

    browser.visit(image_url)
    image_html = browser.html
    soup = bs(image_html, 'html.parser')

    mars_weather = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(mars_weather)
    mars_weather = browser.html
    soup = bs(mars_weather, 'html.parser')

    latest_mars_weather = soup.find("p", class_="TweetTextSize TweetTextSize--normal js-tweet-text tweet-text").text
    print(latest_mars_weather)

    mars_facts_url = "https://space-facts.com/mars/"
    facts = pd.read_html(mars_facts_url)
    facts[0]

    mars_hemispheres_url ='https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars' 
    browser.visit(mars_hemispheres_url)

    cerebrus_url = 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/cerberus_enhanced.tif/full.jpg'
    schiaparelli_url = 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/schiaparelli_enhanced.tif/full.jpg'
    syrtis_url = 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/syrtis_major_enhanced.tif/full.jpg'
    valles_marineris_url = 'https://astropedia.astrogeology.usgs.gov/download/Mars/Viking/valles_marineris_enhanced.tif/full.jpg'

    hemisphere_image_urls = [
        {"title": "Valles Marineris Hemisphere", "img_url": valles_marineris_url},
        {"title": "Cerberus Hemisphere", "img_url": cerebrus_url},
        {"title": "Schiaparelli Hemisphere", "img_url": schiaparelli_url},
        {"title": "Syrtis Major Hemisphere", "img_url": syrtis_url},
    ]

    hemisphere_image_urls
    
    return(hemisphere_image_urls