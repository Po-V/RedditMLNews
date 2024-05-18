# imports
import reddit_scrapper as rc
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

# load environment variables
load_dotenv()

# environment configuration
GROQ_API_KEY = os.getenv('GROQ_API_KEY')

# instantiate llama 3 chat model 
llm = ChatGroq(temperature=0, groq_api_key= GROQ_API_KEY, model_name="llama3-8b-8192")

# scrape subreddit
results = rc.scrape_reddit('MachineLearning')[:-1]

def summarize_post():
    """
    Summarize subreddit posts and comments using llama 3 model
    """
    for result in results:
        print('################################\n')
        print(f"Post title :{result['title']} \n")
        prompt = f"Summarize the following Reddit post in less than 100 words:\n\n{result['title']}\n\n{[result['text']] + result['comments']}"
        summary = llm.invoke([('human',prompt)])
        print("Post TLDR : " + summary.content)
        print('\n')
        

if __name__ == "__main__":
    summarize_post()