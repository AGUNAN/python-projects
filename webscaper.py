import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://www.linkedin.com/jobs/search/?currentJobId=4248118345&geoId=106888327&keywords=python%20developer&origin=JOBS_HOME_KEYWORD_AUTOCOMPLETE&refresh=true')
res2 = requests.get('https://www.linkedin.com/jobs/search/?currentJobId=4248118345&geoId=106888327&keywords=python%20developer&origin=JOBS_HOME_KEYWORD_AUTOCOMPLETE&refresh=true')
soup = BeautifulSoup(res.text, 'html.parser')
soup2 = BeautifulSoup(res2.text, 'html.parser')

links = soup.select('.titleline > a')  # heads up! .storylink changed to .titleline
subtext = soup.select('.subtext')
links2 = soup2.select('.titleline > a')  # heads up! .storylink changed to .titleline
subtext2 = soup2.select('.subtext')

mega_links = links + links2
mega_subtext = subtext + subtext2


def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key=lambda k: k['votes'], reverse=True)


def create_custom_hn(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        title = item.getText()
        href = item.get('href', None)
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 99:
                hn.append({'title': title, 'link': href, 'votes': points})
    return sort_stories_by_votes(hn)


pprint.pprint(create_custom_hn(mega_links, mega_subtext))
