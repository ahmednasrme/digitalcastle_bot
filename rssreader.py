import requests
import xml.etree.ElementTree as ET
import datetime
import os
from dotenv import load_dotenv, dotenv_values
load_dotenv()

rss_feed_urls = os.getenv("FEEDS").split(',')

def request_rss(rss_feed_url):
    response = requests.get(rss_feed_url)
    return response.content

def extract_text(element):
    if element is not None:
        return element.text
    return None

def node_tuples(root):
    items = root.findall('.//item')
    nodes = []
    for item in items:
        title = extract_text(item.find('title'))
        link = extract_text(item.find('link'))
        description = extract_text(item.find('description'))
        if title and link and description:
            nodes.append(f'\n*{title}*\n{description}\n{link}\n')
    return nodes

def articales_links(root):
    items = root.findall('.//item')
    links = []
    for item in items:
        links.append(extract_text(item.find('link')))
    return links

def aggregate_news():
    # Ensure data directory exists
    os.makedirs('data', exist_ok=True)
    
    file_path = f'data/latest{datetime.datetime.date(datetime.datetime.now())}.md'
    
    with open(file_path, 'w', encoding='utf-8') as report:  # Changed to 'w' mode to avoid duplicate entries
        for url in rss_feed_urls:    
            rss_feed = request_rss(url)
            root = ET.fromstring(rss_feed)
            lines = node_tuples(root)  # The file is now handled by the with statement
            report.writelines(['*',lines[0],'*\n',lines[1],'\n',lines[2],'\n'])
    
    return file_path  # Return the path instead of file object

if __name__ == "__main__":
    aggregate_news()
    print('digest created')