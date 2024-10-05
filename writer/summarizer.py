# Set up Gemini API
from dotenv import load_dotenv
import google.generativeai as genai
import os
from opencc import OpenCC

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-1.5-flash-latest")
cc = OpenCC("s2twp")


def summarize_repo(repositories):
    summaries = []
    prompt = """
        ！請確定使用繁體中文zh-TW!確保格式依照我的範本！

        #### 簡介

        #### 主要功能

        #### 如何使用

        - Examine the following README.md content and summarize in 3 parts 簡介 & 主要功能 & 如何使用 in 繁體中文
        - 標題 is link and heading of markdown file.
        - List in bullet points. Every part should be at most 8 points and at most 300 words.
        - Please keep the technical terms in English. 
        - Use markdown to format the content in pretty layout and do not include image.
        - Could include code snippets if necessary.
        - Do not add any additional information.
        - Abstract length should be around 100-200 characters.
        - Do not add any new heading. like ## or ####

        ！確保格式依照我的範本！
    """

    for repository in repositories:
        try:
            if len(summaries) >= 5:
                break

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

        except Exception as e:
            print(e)
            pass

    return summaries
