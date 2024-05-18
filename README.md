# RedditTLDR
This Python project scrapes posts from a specified subreddit and summarizes each post using the Llama 3 model from Groq.

## Features

- Scrapes a specified number of hot title, posts, url and post comments from a given subreddit
- Summarizes the text content of each post using the Llama 3 model using Groq api wrapper from Langchain
- Prints output to the console

## Prerequisites

- Python 3.6 or higher
- Reddit API credentials (client ID and client secret)
- Groq API credentials

## Installation

1. Clone the repository:

```bash
git clone https://github.com/Po-V/RedditTLDR.git
```

2. Navigate to the project directory:

```bash
cd RedditTLDR
```

3. Create a new virtual environment (optional but recommended):

```bash
python -m venv env
```

4. Activate the virtual environment (on Windows):

```bash
env\Scripts\activate
```

5. Install the required dependencies:

```bash
pip install -r requirements.txt
```

6. Create a `.env` file in the project root directory and add your Reddit and Groq API credentials:

```bash
REDDIT_CLIENT_ID=your_reddit_client_id
REDDIT_CLIENT_SECRET=your_reddit_client_secret
GROQ_API_KEY = your_groq_api_key
```

## Usage

Run the main script:

```bash
python main.py
```

The script will scrape the specified number of hot posts from the configured subreddit, summarize the text 
and comments content of each post using the Llama 3 model, and log the post titles and summaries to the console.

