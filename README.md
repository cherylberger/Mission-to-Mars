# Mission to Mars Module 10 - Cheryl Berger

### Overview: 
Robin wants to polish her Mission to Mars WebApp and has asked me to adjust the current web app to include all four of the hemisphere images from an astrogeology site she was browsing recently. To do this, we will use BeautifulSoup and Splinter to scrape full-resolution images of Mars’s hemispheres and the titles of those images, store the scraped data on a Mongo database, use a web application to display the data, and alter the design of the web app to accommodate these images.

###  Results: 

#### Deliverable 1: Scrape Full-Resolution Mars Hemisphere Images andmTitles
Using BeautifulSoup and Splinter, you’ll scrape full-resolution images of Mars’s hemispheres and the titles of those images

![image](https://user-images.githubusercontent.com/94234511/152661063-515c6551-3604-4298-965e-1d1fa4e6ec76.png)
![image](https://user-images.githubusercontent.com/94234511/152661069-1cb2ec20-af32-4a83-a4e5-d7063d2fa289.png)
![image](https://user-images.githubusercontent.com/94234511/152661089-52a82ddb-3014-40cc-9607-cfd91dc1e7e5.png)
![image](https://user-images.githubusercontent.com/94234511/152661099-c15c9f0e-910f-4fcc-bd64-9252a7b12135.png)


![image](https://user-images.githubusercontent.com/94234511/152660829-aea13753-c035-49a5-b8d3-775033457228.png)

![image](https://user-images.githubusercontent.com/94234511/152660806-9f54b841-2789-4469-b371-e10d4ffbaa2e.png)

![image](https://user-images.githubusercontent.com/94234511/152661044-90c67d54-ccd3-42c0-848d-e21638932843.png)

#### Deliverable 2: Update the Web App with Mars’s Hemisphere Images and Titles
Add the code you created in Deliverable 1 to your scraping.py file, update your Mongo database, and modify your index.html file so the webpage contains all the information you collected in this module as well as the full-resolution image and title for each hemisphere image.

Update scraping.py file
![image](https://user-images.githubusercontent.com/94234511/152713542-dcdb7b5f-d8c3-4cbf-8f62-dba75551f863.png)

Update index.html
![image](https://user-images.githubusercontent.com/94234511/152713624-82a816b2-ff15-4f57-b400-d80a3b97b8d3.png)

Export Mission-to-Mars to Python file Mission to Mars.py
![image](https://user-images.githubusercontent.com/94234511/152713705-27eb855b-decd-4697-a08c-c82610a35389.png)

#### Deliverable 3:  
The objective of this deliverable was to update the WebApp to make it mobile responsive and add two additional Bootstrap 3 components to make it
stand out.

  1) The updated code below was added to allow the web app to be mobile responsive

  1) Update the index.html file to make the page header white (Bootstrap 3 component 1)
    ![image](https://user-images.githubusercontent.com/94234511/152711782-5ac4719a-28c9-41a8-a12a-d7d67746cf06.png)

  3) Update the hemisphere url images to change their shape to rounded (Bootstrap 3 component 2)
    ![image](https://user-images.githubusercontent.com/94234511/152711812-50562c22-51b5-4232-b7cc-ffb0b7f67da1.png)

The updated index file is shown below.  
![image](https://user-images.githubusercontent.com/94234511/152711754-871d4700-c7f8-4654-9842-2b67c78a007c.png)


### Summary:

The results of the initial https://redplanetscience.com performed to gather the Mars data are illustrated below
!https://github.com/cherylberger/Mission-to-Mars/blob/main/Mission%20to%20Mars.png

After adding the code to scrape https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars  the images and titles are scraped using app.py.  The data is updated in a MongoDB database and Flask is used to connect to the WebApp and the new scapings are displayed on the page. 

