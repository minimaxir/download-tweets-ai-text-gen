# download-tweets-ai-text-gen

A small Python 3 script to download public Tweets from a given Twitter account into a format suitable for AI text generation tools (such as [gpt-2-simple](https://github.com/minimaxir/gpt-2-simple) for finetuning [GPT-2](https://openai.com/blog/better-language-models/)).

* Retrieves all tweets as a simple CSV with a single CLI command.
* Preprocesses tweets to remove URLs, extra spaces, and optionally usertags/hashtags.
* Saves tweets in batches (i.e. there is an error or you want to end collection early)

You can view examples of AI-generated tweets from datasets retrieved with this tool in the `/examples` folder.

Inspired by popular demand due to the success of [@dril_gpt2](https://twitter.com/dril_gpt2).

## Usage

First, install the Python script dependencies:

```sh
pip3 install twint==2.1.4 fire tqdm
```

Then download the `download_tweets.py` script from this repo.

The script is interacted via a command line interface. After `cd`ing into the directory where the script is stored in a terminal, run:

```sh
python3 download_tweets.py <twitter_username>
```

e.g. If you want to download all tweets (sans retweets/replies/quote tweets) from Twitter user [@dril](https://twitter.com/dril_gpt2), run:

```sh
python3 download_tweets.py dril
```

The script can can also download tweets from multiple usernames at one time.  To do so, first create a text file (.txt) with the list of usernames.  Then, run script referencing the file name:

```sh
python3 download_tweets.py <twitter_usernames_file_name>
```

The tweets will be downloaded to a single-column CSV titled `<usernames>_tweets.csv`.

The parameters you can pass to the command line interface (positionally or explicitly) are:

* username: Username of the account whose tweets or .txt file name with multiple usernames you want to download [required]
* limit: Number of tweets to download [default: all tweets possible]
* include_replies: Include replies from the user in the dataset [default: False]
* strip_usertags: Strips out `@` user tags in the tweet text [default: False]
* strip_hashtags: Strips out `#` hashtags in the tweet text [default: False]

## How to Train an AI on the downloaded tweets

[gpt-2-simple](https://github.com/minimaxir/gpt-2-simple) has a special case for single-column CSVs, where it will automatically process the text for best training and generation. (i.e. by adding `<|startoftext|>` and `<|endoftext|>` to each tweet, allowing independent generation of tweets)

You can use [this Colaboratory notebook](https://colab.research.google.com/drive/1qxcQ2A1nNjFudAGN_mcMOnvV9sF_PkEb) (optimized from the original notebook for this use case) to train the model on your downloaded tweets, and generate massive amounts of Tweets from it. Note that without a lot of data, the model might easily overfit; you may want to train for fewer `steps` (e.g. `500`).

When generating, you'll always need to include certain parameters to decode the tweets, e.g.:

```python
gpt2.generate(sess,
              length=200,
              temperature=0.7,
              prefix='<|startoftext|>',
              truncate='<|endoftext|>',
              include_prefix=False
              )
```

## Helpful Notes

* Retweets are not included in the downloaded dataset. (which is generally a good thing)
* You'll need *thousands* of tweets at minimum to feed to the input model for a good generation results. (ideally 1 MB of input text data, although with tweets that hard to achieve)
* To help you reach the 1 MB of input text data, you can load data from multiple similar Twitter usernames
* The download will likely end much earlier than the theoretical limit (inferred from the user profile) as the limit includes retweets/replies/whatever cache shennanigans Twitter is employing.
* The legalities of distributing downloaded tweets is ambigious, therefore it's recommended avoiding commiting raw Twitter data to GitHub, and is the reason examples of such data is not included in this repo. (AI-generated tweets themselves likely fall under derivative work/parody protected by Fair Use)

## Maintainer/Creator

Max Woolf ([@minimaxir](https://minimaxir.com))

*Max's open-source projects are supported by his [Patreon](https://www.patreon.com/minimaxir) and [GitHub Sponsors](https://github.com/sponsors/minimaxir). If you found this project helpful, any monetary contributions to the Patreon are appreciated and will be put to good creative use.*

## License

MIT

## Disclaimer

This repo has no affiliation with Twitter Inc.