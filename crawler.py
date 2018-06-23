# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup # pip install beautifulsoup4
import requests # pip install requests


# funções modularizadas
import page_title
import page_links

# função crawl
def crawl(start_url):
  seen_urls = set([start_url])
  available_urls = set([start_url])

  while available_urls:
    url = available_urls.pop()

    try:
      content = requests.get(url, timeout=3).text
    except Exception:
      continue
    
    title = page_title.extract_title(content)
    if title:
      print(title)
      print(url)
      print(" ")

    for link in page_links.extract_links(content):
      if link not in seen_urls:
        seen_urls.add(link)
        available_urls.add(link)


try:
  crawl('https://github.com/')
except KeyboardInterrupt:
  print("stopped crawler")