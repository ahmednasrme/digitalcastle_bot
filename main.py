import logging
from datetime import datetime
import rssreader
import chatgpt4
import send_daily
import os

# Set up logging
os.makedirs('logs', exist_ok=True)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    filename=f'logs/workflow_{datetime.now().strftime("%Y%m%d")}.log'
)

def main():
    try:
        # Step 1: Collect content from RSS feeds
        logging.info("Starting RSS content collection")
        digest_file = rssreader.aggregate_news()
        if not digest_file:
            raise Exception("Failed to generate digest file")
        
        # Step 2: Generate message content using ChatGPT
        logging.info("Generating message content with ChatGPT")
        message_file = chatgpt4.create_content(digest_file)
        if not message_file:
            raise Exception("Failed to generate message content")
        
        # Step 3: Send message via Telegram
        logging.info("Sending message via Telegram")
        success = send_daily.send_message(message_file)
        if not success:
            raise Exception("Failed to send message")
        
        logging.info("Workflow completed successfully")
        return True

    except Exception as e:
        logging.error(f"Workflow failed: {str(e)}")
        return False

if __name__ == "__main__":
    main()
