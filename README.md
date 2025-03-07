# Daily Digest TGBot
This is a Telegram bot designed to do the following:
1- Read several rss feeders and write them down in md format `rssreader.py`
2- Using LLM API, it process the rss feed with prompts engineerd for specific outcome `chatgpt4.py`
3- Send the final message to certain chat id (read from env file) `send_daily.py`

This process can be triggered by running `main.py`. Maybe from crontab.
