# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup 

def extract_title(content):
  soup = BeautifulSoup(content, "lxml") # pip install lxml
  tag = soup.find("title", text=True)

  if not tag:
    return None

  return tag.string.strip() # trim() do python