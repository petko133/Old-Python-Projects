from bs4 import BeautifulSoup
import requests
import time
import pandas
from selenium import webdriver

CHROME_DRIVER_PATH = "D:\\chromedriver.exe"
NBA = "https://www.nba.com/stats/"

header = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
}

response = requests.get("https://www.nba.com/stats/")
nba_web_page = response.text

def load_page(URL):
    driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
    driver.get(URL)
    time.sleep(2)
    driver.execute_script("window.scrollTo(0, 300)")
    time.sleep(2)
    driver.execute_script("window.scrollTo(0, 600)")
    time.sleep(2)
    driver.execute_script("window.scrollTo(0, 900)")
    time.sleep(2)
    return driver.page_source

soup = BeautifulSoup(load_page(NBA), "html.parser")

category_header = soup.find_all(name="div", class_="category-header")[0:9:]
category_body = soup.find_all(name="div", class_="category-body")[0:9:]
category_body_ranks = soup.find_all(name="td", class_="category-table__rank")[0:45:]
category_body_names = soup.find_all(name="td", class_="category-table__text")[0:45:]
category_body_score = soup.find_all(name="td", class_="category-table__value")[0:45:]

head = []

for n in category_header:
    heading = n.span
    a = heading.contents
    head.append(a[0].strip())

positions = []
names = []
teams = []
scores = []
for n in category_body_ranks:
    position = n.contents[0]
    positions.append(position)

for n in category_body_names:
    content = n.a
    name = content.contents[0]
    names.append(name)
    team_cont = n.span
    team = team_cont.contents[0]
    teams.append(team)

for n in category_body_score:
    value = n.a
    score = value.contents[0]
    scores.append(score.strip())

data_points = {
        "Postion": "",
        "Name": "",
        "Team": "",
        "Score": ""
    }

def player_points():
    i = 0
    for n in range(5):
        i += 1
        data_points["Postion"] = positions[n]
        data_points["Name"] = names[n]
        data_points["Team"] = teams[n]
        data_points["Score"] = scores[n]
        if i == 1:
            data_points_csv = pandas.DataFrame(data_points, index=[n])
            data_points_csv.to_csv("player_points.csv", mode="w", header=True)
        else:
            data_points_csv = pandas.DataFrame(data_points, index=[n])
            data_points_csv.to_csv("player_points.csv", mode="a", header=False)

def player_rebounds():
    i = 0
    for n in range(5):
        i += 1
        data_points["Postion"] = positions[5+n]
        data_points["Name"] = names[5+n]
        data_points["Team"] = teams[5+n]
        data_points["Score"] = scores[5+n]
        if i == 1:
            data_points_csv = pandas.DataFrame(data_points, index=[n])
            data_points_csv.to_csv("player_rebounds.csv", mode="w", header=True)
        else:
            data_points_csv = pandas.DataFrame(data_points, index=[n])
            data_points_csv.to_csv("player_rebounds.csv", mode="a", header=False)

def player_assists():
    i = 0
    for n in range(5):
        i += 1
        data_points["Postion"] = positions[10+n]
        data_points["Name"] = names[10+n]
        data_points["Team"] = teams[10+n]
        data_points["Score"] = scores[10+n]
        if i == 1:
            data_points_csv = pandas.DataFrame(data_points, index=[n])
            data_points_csv.to_csv("player_assists.csv", mode="w", header=True)
        else:
            data_points_csv = pandas.DataFrame(data_points, index=[n])
            data_points_csv.to_csv("player_assists.csv", mode="a", header=False)

def player_blocks():
    i = 0
    for n in range(5):
        i += 1
        data_points["Postion"] = positions[15+n]
        data_points["Name"] = names[15+n]
        data_points["Team"] = teams[15+n]
        data_points["Score"] = scores[15+n]
        if i == 1:
            data_points_csv = pandas.DataFrame(data_points, index=[n])
            data_points_csv.to_csv("player_blocks.csv", mode="w", header=True)
        else:
            data_points_csv = pandas.DataFrame(data_points, index=[n])
            data_points_csv.to_csv("player_blocks.csv", mode="a", header=False)

def player_steals():
    i = 0
    for n in range(5):
        i += 1
        data_points["Postion"] = positions[20+n]
        data_points["Name"] = names[20+n]
        data_points["Team"] = teams[20+n]
        data_points["Score"] = scores[20+n]
        if i == 1:
            data_points_csv = pandas.DataFrame(data_points, index=[n])
            data_points_csv.to_csv("player_steals.csv", mode="w", header=True)
        else:
            data_points_csv = pandas.DataFrame(data_points, index=[n])
            data_points_csv.to_csv("player_steals.csv", mode="a", header=False)

def player_turnovers():
    i = 0
    for n in range(5):
        i += 1
        data_points["Postion"] = positions[25+n]
        data_points["Name"] = names[25+n]
        data_points["Team"] = teams[25+n]
        data_points["Score"] = scores[25+n]
        if i == 1:
            data_points_csv = pandas.DataFrame(data_points, index=[n])
            data_points_csv.to_csv("player_turnovers.csv", mode="w", header=True)
        else:
            data_points_csv = pandas.DataFrame(data_points, index=[n])
            data_points_csv.to_csv("player_turnovers.csv", mode="a", header=False)

def player_three_pointers():
    i = 0
    for n in range(5):
        i += 1
        data_points["Postion"] = positions[30+n]
        data_points["Name"] = names[30+n]
        data_points["Team"] = teams[30+n]
        data_points["Score"] = scores[30+n]
        if i == 1:
            data_points_csv = pandas.DataFrame(data_points, index=[n])
            data_points_csv.to_csv("player_three_pointers.csv", mode="w", header=True)
        else:
            data_points_csv = pandas.DataFrame(data_points, index=[n])
            data_points_csv.to_csv("player_three_pointers.csv", mode="a", header=False)

def player_free_throws():
    i = 0
    for n in range(5):
        i += 1
        data_points["Postion"] = positions[35+n]
        data_points["Name"] = names[35+n]
        data_points["Team"] = teams[35+n]
        data_points["Score"] = scores[35+n]
        if i == 1:
            data_points_csv = pandas.DataFrame(data_points, index=[n])
            data_points_csv.to_csv("player_free_throws.csv", mode="w", header=True)
        else:
            data_points_csv = pandas.DataFrame(data_points, index=[n])
            data_points_csv.to_csv("player_free_throws.csv", mode="a", header=False)

def player_fantasy_points():
    i = 0
    for n in range(5):
        i += 1
        data_points["Postion"] = positions[40+n]
        data_points["Name"] = names[40+n]
        data_points["Team"] = teams[40+n]
        data_points["Score"] = scores[40+n]
        if i == 1:
            data_points_csv = pandas.DataFrame(data_points, index=[n])
            data_points_csv.to_csv("player_fantasy_points.csv", mode="w", header=True)
        else:
            data_points_csv = pandas.DataFrame(data_points, index=[n])
            data_points_csv.to_csv("player_fantasy_points.csv", mode="a", header=False)

player_points()
player_rebounds()
player_assists()
player_blocks()
player_steals()
player_turnovers()
player_three_pointers()
player_free_throws()
player_fantasy_points()