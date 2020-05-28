from bs4 import BeautifulSoup as bs
from win10toast import ToastNotifier
from urllib.request import urlopen,Request

header = {'User-Agent':'Mozilla'}
request = Request("https://www.worldometers.info/coronavirus/country/nigeria/", headers= header) 
html = urlopen(request)
html.readline()
soup = bs (html, 'html.parser')

new_cases = soup.find("li", {"class":"news_li"}).strong.text.split()[0]
death = list(soup.find("li", {"class":"news_li"}).strong.next_siblings)[1].text.split()[0]

message = "Todays new cases in Nigeria: " + new_cases + "\n Todays new deaths: " + death

ToastNotifier().show_toast(title="Nigerian Covid-19 update", msg= message, duration=10)
