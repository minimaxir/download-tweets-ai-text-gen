import twint
import fire
import re
import csv


def is_reply(tweet):
    """
    Determines if the tweet is a reply to another tweet.
    Requires somewhat hacky heuristics since not included w/ twint
    """

    # If not a reply to another user, there will only be 1 entry in reply_to
    if len(tweet.reply_to) == 1:
        return False

    # Check to see if any of the other users "replied" are in the tweet text
    users = tweet.reply_to[1:]
    conversations = [user['username'] in tweet.tweet for user in users]

    # If any if the usernames are not present in text, then it must be a reply
    if sum(conversations) < len(users):
        return True
    return False


def get_tweets_text(username, limit, pattern, include_replies):
    """
    Returns a list of cleaned Tweets from the specified username.
    """

    c = twint.Config()
    c.Store_object = True
    c.Hide_output = True
    c.Username = username
    c.Limit = limit

    # Run the tweet search (may take awhile)
    print("Retrieving tweets for @{}...".format(username))
    twint.run.Search(c)
    assert len(twint.output.tweets_list) > 0, "No tweets were returned."

    if include_replies:
        tweets = [re.sub(pattern, '', tweet.tweet).strip()
                  for tweet in twint.output.tweets_list
                  if not is_reply(tweet)]
    else:
        tweets = [re.sub(pattern, '', tweet.tweet).strip()
                  for tweet in twint.output.tweets_list]

    return tweets


def download_tweets(username=None, limit=None, include_replies=False,
                    strip_usertags=True, strip_hashtags=False):
    """Generates a twcloud of any public Twitter account or search query!
    See stylecloud docs for additional parameters.
    :param username: Twitter @ username to gather tweets.
    :param limit: # of tweets to gather; None for all tweets.
    :param include_replies: Whether to include replies to other tweets.
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

    tweets = get_tweets_text(username, limit, pattern, include_replies)

    with open('{}_tweets.csv'.format(username), 'w', encoding='utf8') as f:
        w = csv.writer(f)
        w.writerow(['tweets'])  # gpt-2-simple expects a header by default
        for tweet in tweets:
            if tweet != '':
                w.writerow([tweet])


if __name__ == "__main__":
    fire.Fire(download_tweets)
