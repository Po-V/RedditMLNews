# imports 
from langchain.tools import tool
import praw
import langchain
import os
from dotenv import load_dotenv

# load environment variables
load_dotenv()
langchain.verbose = False

# configuration
CLIENT_ID = os.getenv('REDDIT_CLIENT_ID')
CLIENT_SECRET = os.getenv('REDDIT_CLIENT_SECRET')

@tool
def scrape_reddit(subreddit : str) -> list:
    "Scrape comments from subreddit"

    # create reddit scraping instance
    reddit = praw.Reddit(
            client_id= CLIENT_ID,
            client_secret=CLIENT_SECRET,
            user_agent="Reddit Scraper",
        )
    
    try:
        # scrape top 10 posts on subreddit and retrieve title, url, text and comments
        posts = reddit.subreddit(subreddit).hot(limit = 10)
        data = []
        for post in posts:
            post_data = {'title': post.title, 'url': post.url, 'text' : post.selftext, 'comments': []}

            for comment in list(post.comments)[:1]:
                post_data['comments'].append(comment.body)

            data.append(post_data)
        
        return data
        
    except Exception as e:
        return f"Error: {str(e)}"
        