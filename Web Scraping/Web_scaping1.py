import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver


driver = webdriver.Chrome(executable_path="C:/Users/Ezra Muir/Documents/Training-Work/Machine Learning/Web Scraping/chromedriver.exe")

driver.get("https://developers.google.com/machine-learning/crash-course/framing/check-your-understanding")

results = []

content = driver.page_source
soup = BeautifulSoup(content)

# Extracting data
for element in soup.findAll(attrs={'class': 'devsite-breadcrumb-list'}):  # devsite-nav-list
    name = element.find('a')
    if name not in results:
        results.append(name.text)

# for x in results:
#     print(x)
# print(results)

df = pd.DataFrame({'Names': results})
df.to_csv('names.csv', index=False, encoding='utf-8')
