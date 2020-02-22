import os
import tweepy
import json
import boto3
import time
from datetime import datetime, timedelta, timezone

def collect_tweets(keyword, collect_num, consumer_key, consumer_secret, access_token, access_token_secret):
    """
    Collect tweets including keyword

    Return json array
    """


    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)

    public_tweets = [tweet for tweet in tweepy.Cursor(
        api.search,
        q ='{} exclude:retweets'.format(keyword),
        result_type='recent').items(collect_num)
        ]
    #convert tweet data to json array
    json_list = [json.dumps(tweet._json, ensure_ascii = False) for tweet in public_tweets]
    return '[{}]'.format(','.join(json_list))

def create_date_filename():
    JST = timezone(timedelta(hours = +9), 'JST')
    current = datetime.fromtimestamp(time.time(), JST)
    return current.strftime('%Y%m%d_%H%M%S')

def upload_data(bucket_name, file_name, data):
    """
    Upload data to S3

    data is bytes
    """
    s3_clinet = boto3.client('s3')
    s3_clinet.put_object(Body = data, Bucket = bucket_name, Key = file_name)

def main():
    consumer_key = os.getenv('CONSUMER_KEY')
    consumer_secret = os.getenv('CONSUMER_SECRET')
    access_token = os.getenv('ACCESS_TOKEN')
    access_token_secret = os.getenv('ACCESS_TOKEN_SECRET')
    keyword = os.getenv('KEYWORD')
    collect_num = int(os.getenv('COLLECT_NUM', "100"))
    tweet_data = collect_tweets(keyword, collect_num, consumer_key, consumer_secret, access_token, access_token_secret)

    bucket_name = os.getenv('BUCKET_NAME')
    file_name = '{}/{}.json'.format(keyword, create_date_filename())
    upload_data(bucket_name, file_name, tweet_data.encode())

if __name__ == "__main__":
    main()