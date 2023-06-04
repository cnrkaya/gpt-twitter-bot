import tweepy
import openai
import os

from dotenv import load_dotenv

def get_tweet_from_gpt():

    openai.api_key = os.environ.get("OPENAI_API_KEY")

    response = openai.Completion.create(
      model="text-davinci-003",
      prompt='Sen bir filozofsun ve kafa açıcı tweetler atıyorsun. Attığın son tweet: "',
      max_tokens=225,
      temperature=0.7,
      top_p=1,
      frequency_penalty=1.2,
      presence_penalty=1.2,
      n=1,
      best_of=2,
      stream=False,
      stop=['"', '”']
    )

    tweet = response.choices[0].text
    print(tweet)
    return tweet

def send_tweet(text):
    consumer_key = os.environ.get("TWITTER_API_CONSUMER_KEY")
    consumer_secret = os.environ.get("TWITTER_API_CONSUMER_SECRET")
    bearerToken = os.environ.get("TWITTER_API_BEARER_TOKEN")
    access_token = os.environ.get("TWITTER_API_ACCESS_TOKEN")
    access_secret = os.environ.get("TWITTER_API_ACCESS_TOKEN_SECRET")

    client = tweepy.Client(
        bearer_token=bearerToken,
        access_token=access_token,
        access_token_secret=access_secret,
        consumer_key=consumer_key,
        consumer_secret=consumer_secret
    )

    res = client.create_tweet(text=text)
    print(res)

def main():
    tweet = get_tweet_from_gpt()
    send_tweet(tweet)

if __name__ == "__main__":
    main()
