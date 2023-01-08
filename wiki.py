from bs4 import BeautifulSoup
import datetime
import requests

prefix = "https://en.wikipedia.org"
ferrari_url = prefix + "/wiki/Scuderia_Ferrari"
ferrari_html = requests.get(ferrari_url)
ferrari_wiki = BeautifulSoup(ferrari_html.text, "html.parser")

principal_ref = ferrari_wiki.find("td", class_="infobox-data agent").find("a")
principal_url = prefix + principal_ref["href"]
principal_html = requests.get(principal_url)
principal_wiki = BeautifulSoup(principal_html.text, "html.parser")
principal_name = principal_wiki.find(class_="mw-page-title-main")
name = principal_name.text

image_ref = principal_wiki.find(class_="infobox biography vcard").find("a")
image_url = prefix + image_ref["href"]
image_html = requests.get(image_url)
image_wiki = BeautifulSoup(image_html.text, "html.parser")
image_link = image_wiki.find(class_="fullImageLink").find("a")
image = image_link["href"][2:]

tday = datetime.date.today()
principal = {'Mattia Binotto': datetime.date(2019,1,7), 'Frédéric Vasseur': datetime.date(2022,12,13)}
status = None

if name not in principal:
    principal[name] = tday
    status = "Yes!"
elif principal[name] == tday:
    status = "Yes!"
else:
    status = "Not Yet"

days_time = tday - principal[name]
days = days_time.days