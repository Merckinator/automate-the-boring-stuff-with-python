import requests, bs4

res = requests.get('http://chessmaine.net/chessmaine/events/')
res.raise_for_status()
noStarchSoup = bs4.BeautifulSoup(res.text, 'html.parser')
events = noStarchSoup.select('.entry-header')

eventText = []
for item in events:
    eventText.append(item.getText())

for event in eventText:
    print(event)