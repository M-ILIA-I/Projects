import requests
from bs4 import BeautifulSoup

#url = "https://v-minsk.com/Маршруты/Минск/Городок?date=2022-10-23&passengers=1&from=c625144&to=c628155"
#html_doc = requests.get(url)

#soup = BeautifulSoup(html_doc.text, 'html.parser')
#print(soup)
#freePlaces = soup.find("div", class_='MuiContainer-root jss7 MuiContainer-maxWidthLg').find_all("div", class_="jss10")[1].text.split(" ")[9][0]
#print(int(freePlaces))

text = requests.get("https://v-minsk.com/Маршруты/Минск/Городок?date=2022-11-04&passengers=1&from=c625144&to=c628155")
soup2 = BeautifulSoup(text.text, 'html.parser')

ddd = soup2.find("div", class_='MuiContainer-root jss7 MuiContainer-maxWidthLg').find_all("div", class_="jss10")[1]
print((ddd))

print(ddd.find("div", class_="jss157"))
# print(ddd.find("div", class_="jss157").find("span").text)





#print(ddd.find("div", class_="jss2924"))



