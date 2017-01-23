import sys

from util import get_tweet_by_id


def main(in_stream, out_stream):
    for line in in_stream:
        tweet_ids = line.strip().split('\t')
        tweets = map(get_tweet_by_id, tweet_ids)
        if None in tweets:
            continue
        print >>out_stream, '\t'.join(tweets)


if __name__ == '__main__':
    main(sys.stdin, sys.stdout)

