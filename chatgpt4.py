import requests
import os
import rssreader
import time
import datetime
from dotenv import load_dotenv, dotenv_values
load_dotenv()

def Chatgpt4(prompt):
    url = "https://chatgpt-42.p.rapidapi.com/gpt4"
    payload = {
	"messages": [
		{
			"role": "user",
			"content": prompt
		}
	],
	"web_access": False
    }
    headers = {
	"x-rapidapi-key": os.getenv("x-rapidapi-key"),
	"x-rapidapi-host": "chatgpt-42.p.rapidapi.com",
    "Content-Type": "application/json"
    }
    response = requests.post(url, json=payload, headers=headers)
    #print(response.json())
    return(response.json()['result'])

def create_content(digest_file):
    digest = open(digest_file,'r',encoding='utf-8')
    text = digest.read()
    links = (Chatgpt4(f'''
                      You are an editor for college bulletin board magazine about cyber security.
                    Those are stories from cybersecurity websites,  I want you to choose five stories, which are most important, fresh and catchy to present on our magazine.
                    I want the result to be in json text including only links. don't include anything else in your response as it will be read by a script.
                    {text}
                    ''')
    )
    print(links)
    time.sleep(10)
    message = Chatgpt4(f'''
                 I will provide list of links for news, I want you to provide title and brief in Arabic, dont write anything other than the list, in markdown as the following:
                 ```
                 *title*
                 Brief of the article no more than 250 words
                 link
                 ```
                 {links}
                 ''')
    # write in text file
    file_path = f'data/message{datetime.datetime.date(datetime.datetime.now())}.md'
    file = open(file_path,'w',encoding='utf-8')
    file.writelines(message)
    return file_path

if __name__=='__main__':
    create_content()