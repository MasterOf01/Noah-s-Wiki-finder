import wikipediaapi
import time
from queue import Queue

user_agent="Noah's Wiki Finder (noahhagiwara01@gmail.com)"
wiki=wikipediaapi.Wikipedia(user_agent,"en")

def fetch_links(page):
    links_list=[]
    links=page.links
    for title in links.keys():
        links_list.append(title)
    return links_list

def wikipedia_solver(star_page, target_page):
    print("Loading...")
    start_time=time.time()

    visited = set()
    queue=Queue()
    parent={}

    queue.put(start_page.title)
    visited.add(start_page.title)

    while not queue.empty():
        #get next otem in our queue
        current_page_title=queue.get()
        if current_page_title==target_page.title:
            break

        #fetch all links for current page
        current_page=wiki.page(current_page_title)
        links=fetch_links(current_page)

        #go through each link link on the page
        for link in links:
            if link not in visited:
                queue.put(link)
                visited.add(link)
                parent[link]=current_page_title
    path=[]
    page_title=target_page.title
    while page_title != start_page.title:
        path.append(page_title)
        page_title = parent[page_title]

    path.append(start_page.title)
    path.reverse()

    end_time=time.time()
    print("you wasted,", end_time-start_time, "seconds of my time!!!")
    return path

#creating start and target pages
start_page=wiki.page("Pasadena High School (California)")
target_page=wiki.page("World War II")
path=wikipedia_solver(start_page, target_page)

print(path)