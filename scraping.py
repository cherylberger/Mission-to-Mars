#!/usr/bin/env python
# coding: utf-8

# In[23]:
# Import Splinter and BeautifulSoup as well as Pandas and datetime
from splinter import Browser
from bs4 import BeautifulSoup as soup
import pandas as pd
import datetime as dt
from webdriver_manager.chrome import ChromeDriverManager

# In[9]:
# Set-up the executable path & set-up url for scraping
# executable_path = {'executable_path': ChromeDriverManager().install()}
# browser = Browser('chrome', **executable_path, headless=False)

# Add the function to initialize the browser, create the data dict, end the WebDriver and return the scraped data 
def scrape_all():
    # Initiate headless driver for deployment
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=True)

    # Set the news_title and paragraph variables and tell Python to use the mars_news function to pull the data
    news_title, news_paragraph = mars_news(browser)
    
    # Run all scraping functions and store results in dictionary
data = {
      "news_title": news_title,
      "news_paragraph": news_paragraph,
      "featured_image": featured_image(browser),
      "facts": mars_facts(),
      "last_modified": dt.datetime.now()
}
    
# In[26]:
# Stop webdriver and return data
browser.quit()
  return data
    
# Define the function and indent the code to adhere to the function syntax
# def mars_news():
# Then, add the agrument to the function
def mars_news(browser):
    
    # In[10]:
    # Visit the mars nasa news site
    url = 'https://redplanetscience.com'
    browser.visit(url)

    # Optional delay for loading the page
    browser.is_element_present_by_css('div.list_text', wait_time=1)


    # In[12]:
    # Convert the browser html to a soup object and then quit the browser
    html = browser.html
    news_soup = soup(html, 'html.parser')
    
     # Add try/except for error handling and comment out original code
    try:
        slide_elem = news_soup.select_one('div.list_text')
        # Use the parent element to find the first 'a' tag and save it as 'news_title'
        news_title = slide_elem.find('div', class_='content_title').get_text()
        # Use the parent element to find the paragraph text
        news_p = slide_elem.find('div', class_='article_teaser_body').get_text()  
    
    # slide_elem = news_soup.select_one('div.list_text')


    # In[13]:
    # slide_elem.find('div', class_='content_title')


    # In[14]:
    # Use the parent element to find the first `a` tag and save it as `news_title`
    # news_title = slide_elem.find('div', class_='content_title').get_text()
    # news_title


    # In[15]:
    # Use the parent element to find the paragraph text
    # news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
    # news_p

    except AttributeError:
        return None, None 
    
    
    # Once the function is created, remove the paragraph and image titles from the code and move them to the return function
    return news_title, news_p

# #### Featured Images ####

# In[17]:
# Define the function and add the argument to the function (browser)
def featured_image(browser):

    # Visit URL
    url = 'https://spaceimages-mars.com'
    browser.visit(url)


    # In[18]:
    # Find and click the full image button
    full_image_elem = browser.find_by_tag('button')[1]
    full_image_elem.click()


    # In[19]:
    # Parse the resulting html with soup
    html = browser.html
    img_soup = soup(html, 'html.parser')
    
    try:
   # find the relative image url
   img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')

    except AttributeError:
       return None

    # In[21]:
    # Use the base URL to create an absolute URL
    img_url = f'https://spaceimages-mars.com/{img_url_rel}'
    
    # Return(print) the image, img_url
    return img_url

#     ### Mars Facts ###

# In[24]:
# df = pd.read_html('https://galaxyfacts-mars.com')[0]
# df.columns=['description', 'Mars', 'Earth']
# df.set_index('description', inplace=True)
# df

# In[25]:
# df.to_html()

def mars_facts():
    # Add try/except for error handling
    try:
        # Use 'read_html' to scrape the facts table into a dataframe
        df = pd.read_html('https://galaxyfacts-mars.com')[0]

    except BaseException:
        return None

    # Assign columns and set index of dataframe
    df.columns=['Description', 'Mars', 'Earth']
    df.set_index('Description', inplace=True)

    # Convert dataframe into HTML format, add bootstrap
    return df.to_html(classes="table table-striped")


# Tell Flask that script is complete and ready for action
if __name__ == "__main__":
    
    # If running as script, print scraped data
    print(scrape_all())





