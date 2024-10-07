import wikipediaapi
import time

user_agent="Noah's Wiki Finder (noahhagiwara01@gmail.com)"
wiki=wikipediaapi.Wikipedia(user_agent,"en")

def fetch_links(page):
    links_list=[]
    links=page.links
    for title in links.keys():
        links_list.append(title)
    return links_list

#creating start and target pages
start_page=wiki.page("Sushi")
target_page=wiki.page("futomaki")

print(fetch_links(start_page))