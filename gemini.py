import base64
import datetime
import os
from google import genai
from google.genai import types
from dotenv import load_dotenv, dotenv_values
load_dotenv()

def generate(digest_file):
    digest = open(digest_file,'r',encoding='utf-8')
    feed = digest.read()
    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

    response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=[f""" You are an editor for college bulletin board magazine about cyber security.
Those are stories from cybersecurity websites,  I want you to choose seven stories, which are most important, fresh and catchy to present on our magazine.
Don't repeat any redundant news, in case of which, put one title and one summary and corresponded links.
I want the result to be in markdown text. I want you to provide title and brief transelated to Arabic, dont write anything other than the list, answer in markdown as the following without the code fence:
```markdown
*title in Arabic*
Brief of the article in Arabic no more than 250 words
link
```                                     
{feed}
"""])

    # write in text file
    file_path = f'data/message{datetime.datetime.date(datetime.datetime.now())}.md'
    file = open(file_path,'w',encoding='utf-8')
    file.writelines(response.text)
    return file_path

if __name__ == "__main__":
    feed = open('data/latest2025-03-19.md','r',encoding='utf-8').read()
    print(generate(feed))
    
