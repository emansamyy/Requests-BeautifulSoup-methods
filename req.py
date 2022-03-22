# -*- coding: utf-8 -*-
"""
Created on Tue Mar 22 14:44:10 2022

@author: User
"""

import requests #a library that allows you to send HTTP/1.1 requests
#sending a get request to check if a web portal is up


from bs4 import BeautifulSoup #a library for pulling data
#out of html and xml files



response = requests.get('http://localhost')

print(response)

#making a simple HTTP POST method

# r = requests.post(url, data = {'key': 'value'})

#making other types of requests:

# r = requests.delete(url)

# r = requests.head(url) asks for a response identical to
#that of a get request but without the response body

# r = requests.options(url) used for describing communication options for the 
#target resource


#checking which server software the target is using
print(response.headers.get('server'))


#printing response headers of the GET response
print(response.headers)

#get the text content of required page

print(response.text)

#printing the response in a pretty form

soup = BeautifulSoup(response.text , 'html.parser')

print(soup.prettify())

#print the title of that web portal

print(soup.title.string)


#print the urls for images on that page


img_tags = soup.find_all('img')
urls = [img['src'] for img in img_tags]

print(urls)

#scrape all URLS from that page

anchors = [a['href'] for a in soup.find_all('a' , href= True) if
           a.text.strip()]

anchor_set = set(anchors) #turning it into a set of distinct elements

for link in anchor_set:
    print(link)



