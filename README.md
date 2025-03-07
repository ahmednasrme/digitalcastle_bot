# Daily Digest TGBot
This is a Telegram bot designed to do the following:
1. Read several RSS feeders and write them down in MD format (`rssreader.py`)
2. Using LLM API, process the RSS feed with prompts engineered for specific outcomes (`chatgpt4.py`)
3. Send the final message to a certain chat ID (read from env file) (`send_daily.py`)

This process can be triggered by running `main.py`. Maybe from crontab.
