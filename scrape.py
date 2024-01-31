from bs4 import BeautifulSoup
import requests, pandas as pd
columns = ['Fact']
df = pd.DataFrame(columns=columns)

url = "https://www.thefactsite.com/1000-interesting-facts/"
page = requests.get(url)
html_content = page.content.decode('utf-8')  
soup = BeautifulSoup(html_content, 'html.parser')
#want p tag with only list classs
list_paragraphs = soup.find_all('p', class_='list')
for paragraph in list_paragraphs:
    text = paragraph.text
    df_length = len(df)
    data = [text]
    df.loc[df_length]= data

df.to_csv(r'D:\Self_learning\practice_projects\output\facts.csv',encoding='utf-8-sig', index=False)
    
    