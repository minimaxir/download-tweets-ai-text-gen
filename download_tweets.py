import twint
import fire
import re
import csv


def get_tweets_text(username, limit, pattern):
    """
    Returns a list of cleaned Tweets from the specified username.
    """

    c = twint.Config()
    c.Store_object = True
    c.Hide_output = True
    c.Username = username
    c.Limit = limit
    c.Custom["tweet"] = ["tweet"]

    # Run the tweet search (may take awhile)
    print("Retrieving tweets for @{}...".format(username))
    twint.run.Search(c)
    assert len(twint.output.tweets_list) > 0, "No tweets were returned."

    tweets = [re.sub(pattern, '', tweet.tweet).strip()
              for tweet in twint.output.tweets_list]

    return tweets


def download_tweets(username=None, limit=None,
                    strip_usertags=True, strip_hashtags=False):
    """Generates a twcloud of any public Twitter account or search query!
    See stylecloud docs for additional parameters.
    :param username: Twitter @ username to gather tweets.
    :param limit: # of tweets to gather; None for all tweets.
    :param strip_usertags: Whether to remove user tags from the tweets.
    :param strip_hashtags: Whether to remove hashtags from the tweets.
    """

    assert username, "You must specify a username to download tweets from."
    if limit:
        assert limit % 20 == 0, "`limit` must be a multiple of 20."

    pattern = r'http\S+|pic.\S+|\xa0|…'

    if strip_usertags:
        pattern += r'|@[a-zA-Z0-9_]+'

    if strip_hashtags:
        pattern += r'|#[a-zA-Z0-9_]+'

    tweets = get_tweets_text(username, limit, pattern)

    with open('{}_tweets.csv'.format(username), 'w', encoding='utf8') as f:
        w = csv.writer(f)
        w.writerow(['tweets'])  # gpt-2-simple expects a header by default
        for tweet in tweets:
            if tweet != '':
                w.writerow([tweet])


if __name__ == "__main__":
    fire.Fire(download_tweets)
