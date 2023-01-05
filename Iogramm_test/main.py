from bs4 import BeautifulSoup
import requests
import json
import time



def get_text(url):
    s = requests.session()
    response = s.get(url=url)
    bs = BeautifulSoup(response.text, "html.parser")
    tag = bs.find("div", class_="MuiContainer-root jss7 MuiContainer-maxWidthLg").find_all("div", class_="jss10")[2]
    tag = tag.find_all("div", class_="MuiGrid-root MuiGrid-item MuiGrid-grid-md-auto")[1]
    return tag.text




def main():
    url = "https://v-minsk.com/Маршруты/Минск/Городок?date=2022-11-04&passengers=1&from=c625144&to=c628155"
    text = get_text(url)
    if text != "Нет мест":
        print("Реще заказывай билет...")
    else:
        print("Билетов все еще нет...")



if __name__ == "__main__":
    main()