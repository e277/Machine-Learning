import requests
from bs4 import BeautifulSoup


response = requests.get('https://oxylabs.io/')
# # print(response.status_code)
# # print(response.text)

# # POST
# form_data = {'key1': 'value1', 'key2': 'value2'}
# response = requests.post('https://oxylabs.io/', data=form_data)
# # print(response.text)

# proxies = {'http' : 'http://user:password@proxy.oxylabs.io'}
# response = requests.get('https://oxylabs.io/', proxies=proxies)
# print(response.text)

soup = BeautifulSoup(response.text, 'html.parser')
# print(soup.title)


blog_titles = soup.findAll('h2', attrs={'class': 'oxy-7g428u'})
for title in blog_titles:
    print(title.text)


page_title = soup.find('h1', attrs={'class': 'oxy-7g428u'}).get_text(strip=True) # return with the element tag
# page_title = soup.find('h1', attrs={'class': 'oxy-7g428u'}) 
print(page_title)


name = 'Ezra'
name = 'Keneil'
print(name)