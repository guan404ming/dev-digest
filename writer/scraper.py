from datetime import datetime, timedelta
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import google.generativeai as genai
import os
from opencc import OpenCC

# Set up Gemini API
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash-latest")
cc = OpenCC("s2twp")

url = "https://github.com/trending?since=weekly"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

repo_links = []
repo_elements = soup.select("a")
for repo_element in repo_elements:
    hydro_click = repo_element.get("data-hydro-click")
    if hydro_click and '"click_target":"REPOSITORY"' in hydro_click:
        repo_links.append(f'https://github.com{repo_element["href"]}')

summaries = []
for repo_link in repo_links:
    if len(summaries) >= 5: 
        break

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
        summaries.append(cc.convert(summary))

# Write summaries to a markdown file
now = datetime.now()
seven_days_ago = now - timedelta(days=6)
file_name = seven_days_ago.strftime("%Y%m%d") + now.strftime("%m%d") + ".mdx"
info = f"""---
title: '[{seven_days_ago.strftime('%-m/%-d')} - {now.strftime('%-m/%-d')}] GitHub Weekly Digest - Flash'
publishedAt: '{datetime.now().strftime("%Y-%m-%d")}'
---
"""

with open("blog/app/blog/posts/" + file_name, "w") as file:
    file.write(info)
    for summary in summaries:
        file.write(summary + "\n")
