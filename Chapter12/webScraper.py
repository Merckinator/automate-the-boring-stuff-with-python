import requests, bs4

res = requests.get('http://chessmaine.net/chessmaine/events/')
res.raise_for_status()
noStarchSoup = bs4.BeautifulSoup(res.text, 'html.parser')
events = noStarchSoup.select('.entry-header')

eventText = [ item.getText() for item in events ]

for event in eventText:
    print(event)

'''
Compare first event scraped to first event saved,
    if they're the same then move along,
    if they're different then see if the scraped event is saved (as not first),
        if so, one was inserted beforehand,
        if not, it must've been inserted
'''