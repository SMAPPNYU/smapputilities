import argparse
import datetime
import logging
import urllib
import json
import csv
import sys
import os

from tkpool.tkpool.tweepypool import TweepyPool
from tweepy import Cursor, TweepError

def twitter_query(output, file_input, auth_file):
    logger = logging.getLogger(__name__)
    
    terms_list = get_terms_list(file_input)
    logger.info('creating oauth pool...')

    #query the tweets
    query_search_tweets(output, terms_list, auth_file)

# problem here is that were using a method that doesnt exist in tweepy 2.3 we need to rewrite the tweepy pool
# its long overdue.
def query_search_tweets(output, terms_list, auth_file):

    logger = logging.getLogger(__name__)

    num_inputs_queried = 0

    #create the api pool
    api_pool = TweepyPool(auth_file)
    write_fd = open(output, 'w+')

    hundred_terms = []

    for term in terms_list:
        if len(hundred_terms) == 100:
            num_inputs_queried = num_inputs_queried + 1
            count = 0
            if not term == '':
                try:
                    for item in api_pool.statuses_lookup(hundred_terms):
                        print(item)
                        logger.debug('tweet text: %s', item.text) 
                        count = count + 1
                        tweet_item = json.loads(json.dumps(item._json))
                        tweet_item['smapp_term'] = term
                        tweet_item['smapp_count'] = count
                        tweet_item['smapp_timestamp'] = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S +0000')
                        write_fd.write(json.dumps(tweet_item))
                        write_fd.write('\n')
                except TweepError as e:
                    logger.info('tweepy error: %s', e)
                logger.info('counted %s objects for input %s', count, term)
            logger.info('number of inputs queried so far: %s', num_inputs_queried)
            # if we come in and the list already has 100, that means
            # we queried that 100
            hundred_terms = [term]
        else:
            hundred_terms.append(term)
    write_fd.close()

def get_terms_list(file_input):
    logger = logging.getLogger(__name__)
    filename, file_extension = os.path.splitext(file_input)
    terms_list = []
    if file_extension == '.json':
        logger.info('loading json...')
        with open(file_input) as data:
            terms_list = json.load(data)
    elif file_extension == '.csv':
        logger.info('loading csv...')
        count = 0
        with open(file_input) as f:
            for rowdict in list(csv.DictReader(f)):
                # if list is not empty
                if rowdict:
                    terms_list.append(rowdict['term'])
        logger.info('launching query for %s inputs', len(terms_list))
    return terms_list

def parse_args(args):
    currentdate = datetime.datetime.now().strftime("%Y-%m-%d_%H:%M")
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', dest='input', required=True, help='This is a path to your input.json, a [] list of twitter ids.')
    parser.add_argument('-o', '--output', dest='output', required=True, help='This will be your output file, a {} json object showing original ids and twitter screen names.')
    parser.add_argument('-a', '--auth', dest='auth', required=True, help='This is the path to your oauth.json file for twitter')
    parser.add_argument('-l', '--log', dest='log', default=os.path.expanduser('~/pylogs/query_tweet_objects'+currentdate+'.log'), help='This is the path to where your output log should be. Required')
    return parser.parse_args()

if __name__ == '__main__':
    #setup parser for command line arguments
    args = parse_args(sys.argv[1:])
    #configure logs
    logging.basicConfig(filename=args.log, level=logging.INFO)
    # actually merge the bson files
    twitter_query(args.output, args.input, args.auth)

'''
author @yvan
http://tweepy.readthedocs.org/en/v3.5.0/api.html?highlight=search#API.search
https://dev.twitter.com/rest/public/search
https://dev.twitter.com/rest/reference/get/search/tweets
https://dev.twitter.com/rest/public/rate-limiting
'''
