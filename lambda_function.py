import tweet_collector

def lambda_handler(event, context):
    tweet_collector.main()
