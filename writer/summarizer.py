# Set up Gemini API
from dotenv import load_dotenv
from google import genai
import os
from opencc import OpenCC

load_dotenv()

# Create a single client object
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
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
            response = client.models.generate_content(
                model="gemini-2.5-flash", contents=prompt + repository["readme"]
            )
            summary = cc.convert(response.text.strip())

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
