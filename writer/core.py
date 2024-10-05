from datetime import datetime, timedelta
from scraper import scrape_repo
from summarizer import summarize_repo

repositories = scrape_repo()
summaries = summarize_repo(repositories)

# Write summaries to a markdown file
now = datetime.now()
seven_days_ago = now - timedelta(days=6)
file_name = seven_days_ago.strftime("%Y%m%d") + now.strftime("%m%d") + ".mdx"
info = f"""---
title: '[{seven_days_ago.strftime('%-m/%-d')} - {now.strftime('%-m/%-d')}] GitHub Weekly Digest'
publishedAt: '{datetime.now().strftime("%Y-%m-%d")}'
---
"""

with open(f"frontend/app/blog/posts/{file_name}", "w") as file:
    file.write(info)
    for summary in summaries:
        repository = summary["repository"]

        file.write(
            f"## 📌 [{repository["title"]}]({f'https://github.com{repository["link"]}'})"
        )
        file.write(f"""
<Callout>
    {'Description: ' + repository["description"] + "\\" if repository["description"] else ''}
    🌐 {repository["language"]}｜⭐️ {repository["stars"]} | {repository["week_stars"]} stars this week
</Callout>
    """)
        file.write(summary["summary"] + "\n")
