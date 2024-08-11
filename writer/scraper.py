from datetime import datetime
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import google.generativeai as genai
import os

# Set up Gemini API
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash-latest")

url = "https://github.com/trending?since=weekly"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

repo_links = []
repo_elements = soup.select("a")
for repo_element in repo_elements:
    hydro_click = repo_element.get("data-hydro-click")
    if hydro_click and '"click_target":"REPOSITORY"' in hydro_click:
        repo_links.append(f'https://github.com{repo_element["href"]}')

info = f"""
---
title: '[8/5 - 8/11] GitHub Weekly Digest'
publishedAt: '{datetime.now().strftime("%Y-%m-%d")}'
---
"""
print(info)

count = 0
for repo_link in repo_links:
    soup = BeautifulSoup(requests.get(repo_link).text, "html.parser")
    
    for element in ["article", "pre"]:
        readme_elements = soup.select(element)
        if len(readme_elements) > 0:
            readme_text = readme_elements[0].text
            break
    else:
        continue
    
    prompt = f"""
    ！請確定使用繁體中文zh-TW！並且確保格式依照我的範本！

    ## 📌 [標題]({repo_link})

    #### 簡介

    #### 主要功能

    #### 如何使用

    - Examine the following README.md content and summarize in 4 parts 標題 & 簡介 & 主要功能 & 如何使用 in 繁體中文
    - List in bullet points. Every part should be at most 8 points.
    - Please keep the technical terms in English. 
    - Use markdown to format the content in pretty layout and do not include image.
    - Could include code snippets if necessary.
    - Do not add any additional information.
    - Abstract length should be around 200-300 characters.
    - Do not add any new heading. like ## or ####

    ！請確定使用繁體中文zh-TW！並且確保格式依照我的範本！
    """
    summary = model.generate_content(prompt + readme_text).text.strip()
    
    if len(summary) > 0:
        print(summary)
        count += 1
    
    if count == 2:
        break
