# tweet_collector
- Search tweet using Twitter API
- Store them to S3

# How to run
```
$ poetry install

# You need aws credential
$ poetry run python tweet_collector.py
```

# Environment variables
|Name|Description|
|--|--
|CONSUMER_KEY|consumer key of twitter api
|CONSUMER_SECRET|consumer secret of twitter api
|ACCESS_TOKEN|access token of twitter api
|ACCESS_SECRET|access secret of twitter api
|KEYWORD|Search keyword when searching twitter
|COLLECT_NUM|The number of tweets to be collected
|BUCKET_NAME|S3 bucket name