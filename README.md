# download-tweets-ai-text-gen

A small Python 3 script to download public Tweets from a given Twitter account into a format sutiable for training with AI text generation tools (such as [gpt-2-simple](https://github.com/minimaxir/gpt-2-simple)):

* Retrieves all tweets as a simple CSV with a single CLI command.
* Preprocesses tweets to remove URLs, extra spaces, and optionally usertags/hashtags.
* Saves tweets in batches (i.e. there is an error)

Inspired by popular demand due to the success of [@dril_gpt2](https://twitter.com/dril_gpt2)

## Usage

First, install the Python script dependencies:

```sh
pip3 install twint fire tqdm
```

Then download the `download_tweets.py` script from this repo.

The script is interacted via a command line interface. After `cd`ing into the directory where the script is stored in a terminal, run:

```sh
python3 download_tweets.py <twitter_username>
```

e.g. If you want to download *all* tweets from Twitter user @dril, run:

```sh
python3 download_tweets.py dril
```

The parameters you can pass to the command line interface (positionally or explicitly) are:

* username: Username of the account whose tweets you want to download [required]
* limit: Number of tweets to download [default: all tweets possible]
* include_replies: Include replies and quote tweets from the user in the dataset [default: False]
* strip_usertags: Strips out `@` user tags in the tweet text [default: True]
* strip_hashtags: Strips out `#` hashtags in the tweet text [default: False]

## Helpful Notes

* You'll need *thousands* of tweets at minimum to feed to the input model for a good generation results. (ideally 1 MB of input text data)
* The script queries about 17 tweets per second, which may mean it'll take 10+ minutes for a dataset large enough to train an AI network.

## Maintainer/Creator

Max Woolf ([@minimaxir](https://minimaxir.com))

*Max's open-source projects are supported by his [Patreon](https://www.patreon.com/minimaxir) and [GitHub Sponsors](https://github.com/sponsors/minimaxir). If you found this project helpful, any monetary contributions to the Patreon are appreciated and will be put to good creative use.*

## License

MIT

## Disclaimer

This repo has no affiliation with Twitter Inc.