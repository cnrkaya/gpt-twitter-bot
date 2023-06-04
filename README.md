# gpt-twitter-bot
The project consists of a Python script that interacts with the OpenAI API to fetch tweet text generated by the GPT-3.5 model. It then uses the Tweepy library to communicate with the Twitter API and post the generated tweets.

## Features

- Generates philosophical and thought-provoking tweets using the GPT-3.5 model.
- Posts tweets automatically to Twitter using the Twitter API.
- Customizable prompts and configurations to create unique tweets.

## Requirements
* Python 3.7 or higher

## Installation

1. Clone the repository:

```bash
git clone https://github.com/cnrkaya/gpt-twitter-bot.git
```

2. Install the required dependencies:

```bash
pip3 install -r requirements.txt
```

3. Set up your environment variables:

Open a terminal and export your environment variables using the following commands, replacing your_value with your actual values:
```bash
export OPENAI_API_KEY=your_openai_api_key
export TWITTER_API_CONSUMER_KEY=your_twitter_consumer_key
export TWITTER_API_CONSUMER_SECRET=your_twitter_consumer_secret
export TWITTER_API_BEARER_TOKEN=your_twitter_bearer_token
export TWITTER_API_ACCESS_TOKEN=your_twitter_access_token
export TWITTER_API_ACCESS_TOKEN_SECRET=your_twitter_access_token_secret
```

## Usage

Run the script:

```bash
python3 philo_bot_tweet.py
```
