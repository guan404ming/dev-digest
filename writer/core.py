from datetime import datetime, timedelta
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import google.generativeai as genai
import os
from opencc import OpenCC

from scraper import scraper

# Set up Gemini API
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash-latest")
cc = OpenCC("s2twp")

# Scrape GitHub trending repositories
repositories = scraper()

summaries = []
for repository in repositories:
    if len(summaries) >= 5:
        break

    prompt = """
    ！請確定使用繁體中文zh-TW!確保格式依照我的範本！

    #### 簡介

    #### 主要功能

    #### 如何使用

    - Examine the following README.md content and summarize in 3 parts 簡介 & 主要功能 & 如何使用 in 繁體中文
    - 標題 is link and heading of markdown file.
    - List in bullet points. Every part should be at most 8 points.
    - Please keep the technical terms in English. 
    - Use markdown to format the content in pretty layout and do not include image.
    - Could include code snippets if necessary.
    - Do not add any additional information.
    - Abstract length should be around 100-200 characters.
    - Do not add any new heading. like ## or ####

    ！確保格式依照我的範本！
    """
    summary = cc.convert(
        model.generate_content(prompt + repository["readme"]).text.strip()
    )

    if len(summary) > 0:
        summaries.append(
            {
                "repository": repository,
                "summary": summary,
            }
        )

# Write summaries to a markdown file
now = datetime.now()
seven_days_ago = now - timedelta(days=6)
file_name = seven_days_ago.strftime("%Y%m%d") + now.strftime("%m%d") + ".mdx"
info = f"""---
title: '[{seven_days_ago.strftime('%-m/%-d')} - {now.strftime('%-m/%-d')}] GitHub Weekly Digest'
publishedAt: '{datetime.now().strftime("%Y-%m-%d")}'
---
"""

with open("blog/app/blog/posts/" + file_name, "w") as file:
    file.write(info)
    for summary in summaries:
        repository = summary["repository"]

        file.write(
            f"## 📌 [{repository["title"]}]({f'https://github.com{repository["link"]}'})"
        )
        file.write(f"""
<Callout>
    Desription: {repository["description"]}\\
    🌐 {repository["language"]}｜⭐️ {repository["stars"]}
</Callout>
""")
        file.write(summary["summary"] + "\n")
