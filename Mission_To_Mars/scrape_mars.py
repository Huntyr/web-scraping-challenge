from bs4 import BeautifulSoup as bs
import pandas as pd
from splinter import Browser
import requests
import time


# def init_browser():
#     executable_path = {"executable_path": "/chromedriver"}
#     return Browser("chrome", **executable_path, headless=False)

def scrape():
    # In[3]:
   

    #1.1 MARS NEWS------------------------------
    # get latest news from nasa mars exploration page at https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest
    mars_news_url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'

    # set up a Browser to get access to js stuff
    executable_path = {"executable_path": "/chromedriver"}
    browser = Browser("chrome", **executable_path, headless=False)


    # In[4]:


    # visit the website
    browser.visit(mars_news_url)


    # In[5]:


    nasa_news = browser.html
    soup_nasa_news = bs(nasa_news, 'html.parser')
    nasa_news_title = soup_nasa_news.find('div', class_='content_title').text.strip()
    #nasa_news_teaser = soup_nasa_news.find('div', class_="artlce_teaser_body").text.strip()
    nasa_news_teaser = soup_nasa_news.find('div', class_='article_teaser_body').text
    # .find('li', class_='slide').find('div', class_='list_text')

    # print(nasa_news_title)
    # print(nasa_news_teaser)


    # In[6]:


    # 1.2 JPL Mars space images
    # Visit the url for JPL Featured Space Image https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars.
    # Use splinter to navigate the site and find the image url for the current Featured Mars Image and assign the url string to a variable called featured_image_url.
    # Make sure to find the image url to the full size .jpg image.
    # Make sure to save a complete url string for this image.
    nasa_image_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(nasa_image_url)


    # In[7]:


    button = browser.find_by_id('full_image')
    button.click()


    # In[8]:


    button1 = browser.find_by_text('more info     ')
    button1.click()


    # In[9]:


    featured_image_url = browser.find_link_by_partial_href('spaceimages/images')
    #jpl_image = browser.html
    #soup_jpl_image = bs(jpl_image, 'html.parser')
    #soup_jpl_image
    featured_image_url = featured_image_url['href']


    # In[10]:


    # Mars Weather
    # Visit the Mars Weather twitter account https://twitter.com/marswxreport?lang=en and scrape the latest Mars weather tweet from the page. 
    # Save the tweet text for the weather report as a variable called mars_weather.
    mars_weather_url = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(mars_weather_url)


    # In[14]:


    html = browser.html
    parsed_tweet = bs(html, 'html.parser')
    mars_weather = parsed_tweet.find('p', class_='tweet-text').text
    # print(mars_weather)


    # In[ ]:





    # In[15]:


    # Mars Facts
    # Visit the Mars Facts webpage https://space-facts.com/mars/ and use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.
    # Use Pandas to convert the data to a HTML table string.
    mars_facts_url = 'https://space-facts.com/mars/'
    browser.visit(mars_facts_url)


    # In[17]:


    mars_df = pd.read_html(mars_facts_url)
    # print(mars_df)


    # In[18]:


    mars_df[1]


    # In[19]:


    mars_facts_df = mars_df[1]
    mars_facts_df = mars_facts_df.to_html()
    mars_facts_df


    # In[35]:


    #Mars Hemispheres
    # Visit the USGS Astrogeology site https://space-facts.com/mars/ to obtain high resolution images for each of Mar's hemispheres.
    # You will need to click each of the links to the hemispheres in order to find the image url to the full resolution image.
    # Save both the image url string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name. Use a Python dictionary to store the data using the keys img_url and title.
    # Append the dictionary with the image url string and the hemisphere title to a list. This list will contain one dictionary for each hemisphere.
    base_hem_html = 'https://astrogeology.usgs.gov/' # used later
    mars_hem_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(mars_hem_url)


    # In[36]:


    html = browser.html
    hemisphere_parsed = bs(html,"html.parser")


    # In[37]:


    browser.click_link_by_partial_text('Cerberus Hemisphere Enhanced')
    #wait
    # i feel like there should be a "wait" command or something
    time.sleep(1)
    html = browser.html
    page_parsed = bs(html, 'html.parser')


    # In[40]:


    cerberus_image = page_parsed.find('img', class_='wide-image').get('src')
    cerberus_img_html = base_hem_html + cerberus_image
    cerberus_title = page_parsed.find('h2', class_='title').text
    # print(cerberus_img_html)
    # print(cerberus_title)


    # In[45]:


    # rinse-repeat Schiaparelli
    browser.visit(mars_hem_url)
    time.sleep(1)
    html = browser.html
    hemisphere_parsed = bs(html,"html.parser")


    # In[46]:


    browser.click_link_by_partial_text('Schiaparelli Hemisphere Enhanced')
    time.sleep(1)
    html = browser.html
    page_parsed = bs(html, 'html.parser')


    # In[47]:


    schiaparelli_image = page_parsed.find('img', class_='wide-image').get('src')

    schiaparelli_img_html = base_hem_html + schiaparelli_image
    schiaparelli_title = page_parsed.find('h2', class_='title').text
    # print(schiaparelli_img_html)
    # print(schiaparelli_title)


    # In[48]:


    # rinse-repeat Syrtis
    browser.visit(mars_hem_url)
    time.sleep(1)
    html = browser.html
    hemisphere_parsed = bs(html,"html.parser")


    # In[50]:


    browser.click_link_by_partial_text('Syrtis Major Hemisphere Enhanced')
    time.sleep(1)
    html = browser.html
    page_parsed = bs(html, 'html.parser')


    # In[51]:


    syrtis_image = page_parsed.find('img', class_='wide-image').get('src')

    syrtis_img_html = base_hem_html + syrtis_image
    syrtis_title = page_parsed.find('h2', class_='title').text
    # print(syrtis_img_html)
    # print(syrtis_title)


    # In[52]:


    # rinse-repeat Valles
    browser.visit(mars_hem_url)
    time.sleep(1)
    html = browser.html
    hemisphere_parsed = bs(html,"html.parser")


    # In[54]:


    browser.click_link_by_partial_text('Valles Marineris Hemisphere Enhanced')
    time.sleep(1)
    html = browser.html
    page_parsed = bs(html, 'html.parser')


    # In[55]:


    valles_image = page_parsed.find('img', class_='wide-image').get('src')

    valles_img_html = base_hem_html + valles_image
    valles_title = page_parsed.find('h2', class_='title').text
    # print(valles_img_html)
    # print(valles_title)


    # In[57]:


    # bring it all together in a dict
    hs_title_img_final = [
        {"title": cerberus_title, "img_src": cerberus_img_html},
        {"title": schiaparelli_title, "img_src": schiaparelli_img_html},
        {"title": syrtis_title, "img_src": syrtis_img_html},
        {"title": valles_title, "img_src": valles_img_html}
    ]
    # print(hs_title_img_final)


    # In[39]:


    #I could probably loop the above section for all hemispheres, but I can't think of how to do it at the moment

    # hs_titles = []
    # hs_urls = []

    # img_title_loc = hemisphere_parsed.find_all('a', class_='h3')

    # for x in img_title_loc:
    #     hs_title.append(hemisphere_parsed.find('h3').text)
    #     hs_urls.append(base_hem_html + hemisphere_parsed.find('a', class_='href')





    # make dictionary out of all collected data for later use in flask app
    mars_info={"nasa_news_title": nasa_news_title,
            "nasa_news_teaser": nasa_news_teaser,
            "featured_image_url":featured_image_url,
            "mars_weather_url":mars_weather_url,
            "mars_weather":mars_weather,
            "mars_facts_df":mars_facts_df,
            "hs_title_img_final":hs_title_img_final    
            }
    browser.quit()
    return mars_info



