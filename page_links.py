# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup

def extract_links(content):
  soup = BeautifulSoup(content, "lxml") # pip install lxml
  links = set() # set = collection | uma array sem elementos duplicados

  for tag in soup.find_all("a", href=True):
    if tag["href"].startswith("http"):
      links.add(tag["href"])

  return links