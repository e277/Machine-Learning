import requests
from bs4 import BeautifulSoup as bs
import csv


# res = requests.get('https://statinja.gov.jm/Demo_SocialStats/Justice%20and%20Crime.aspx')
res = requests.get('https://www.geeksforgeeks.org/page/')

# print(res)
# print(res.content)
# print(res.url)
# print(res.status_code)

# parsing the html
# soup = bs(res.content, 'html.parser')

# print(soup.prettify())

# print(soup.title)
# print(soup.title.name)
# print(soup.title.parent.name)

# s = soup.find('div', class_='whitebg-border')
# s = soup.find('div', id='ContentPlaceHolder1_dvframeG')
# content = s.find_all('div')
# print(content)

# lines = s.find_all('div')
# for line in lines:
#     print(line.text)

# for link in soup.find_all('a'):
#     print(link.get('href'))

# images_list = []
# images = soup.select('img')
# for image in images:
#     src = image.get('src')
#     alt = image.get('alt')
#     images_list.append({"src": src, "alt": alt})
# for image in images_list:
#     print(image)



soup = bs(res.text, 'html.parser')

# titles = soup.find_all('div', attrs={'class', 'head'})
titles = soup.find_all('div', class_='head')
titles_list = []

count = 1
for title in titles:
	d = {}
	d['Title Number'] = f'Title {count}'
	d['Title Name'] = title.text
	count += 1
	titles_list.append(d)

filename = 'titles.csv'
with open(filename, 'w', newline='') as f:
	w = csv.DictWriter(f,['Title Number','Title Name'])
	w.writeheader()
	
	w.writerows(titles_list)

