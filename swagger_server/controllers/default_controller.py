import connexion
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime
import TwitterAPI
import json
import os.path
from datetime import datetime
from rake_nltk import Rake # https://github.com/csurfer/rake-nltk

# twitter api setup
fn = 'config.json.example'
if os.path.isfile('config.json'):
    fn = 'config.json'

tw_api = TwitterAPI.TwitterAPI(config["consumer_key"], config["consumer_secret"], config["access_token_key"], config["access_token_secret"])

def statuses(username):
    r = api.request("statuses/user_timeline", {"count": tweet_limit, "screen_name": username})
    return r.get_iterator()

def overview(username):
    r = api.request("statuses/user_timeline", {"screen_name": username})
    return r.get_iterator()

def find_closest(alist, target):
    return min(alist, key=lambda x:abs(x-target))

def list_matching(list1, list2):
    list1_copy = list1[:]
    pairs = []
    for i, e in enumerate(list2):
        elem = find_closest(list1_copy, e)
        pairs.append([i, list1.index(elem)])
        list1_copy.remove(elem)
    return pairs

def influencetime(handle, influencer):
    """
    determines how close users tweet to each other

    :param handle: Handle of user to get.
    :type handle: str
    :param influencer: Handle of user to examine influence from.
    :type influencer: str

    :rtype: None
    """
    s1 = [datetime.strptime(t.get("created_at", "-1")) for t in statuses(handle)]
    s2 = [datetime.strptime(t.get("created_at", "-1")) for t in statuses(influencer)]
    return list_matching(s1,s2)


def influencetopic(handle, influencer):
    """
    Determine topic similarity between users

    :param handle: Handle of user to get.
    :type handle: str
    :param influencer: Handle of user to examine influence from.
    :type influencer: str

    :rtype: None
    """
    s1 = [t.text for t in statuses(handle)]
    # Keyword extraction
    r1 = Rake()
    r1.extract_keywords_from_text(" ".join(s1))
    r1.get_ranked_phrases()
    s2 = [t.text for t in statuses(influencer)]
    # Keyword extraction
    r2 = Rake()
    r2.extract_keywords_from_text(" ".join(s2))
    r2.get_ranked_phrases()
    #TODO list comparison
    return 'do some magic!'


def usermentions(handle):
    """
    Get users which a user has mentioned

    :param handle: Handle of user to get.
    :type handle: str

    :rtype: None
    """
    s = [t.entities.get("user_mentions", -1) for t in statuses(handle)]
    return json.dumps(s)


def useroverview(handle):
    """
    Get basic information about a user

    :param handle: Handle of user to get.
    :type handle: str

    :rtype: None
    """
    return json.dumps(overview(handle))


def usertags(handle):
    """
    Get most common recent hashtags used by a user

    :param handle: Handle of user to get.
    :type handle: str

    :rtype: None
    """
    s = [t.entities.hashtags for t in statuses(handle)]
    return json.dumps(s)


def usertimes(handle):
    """
    Gets a picture of when a user tweets

    :param handle: Handle of user to get.
    :type handle: str

    :rtype: None
    """
    s = [t.get("created_at", "-1") for t in statuses(handle)]
    return json.dumps(s)


def usertopics(handle):
    """
    Gets topics a user uses, grouped using word2vec

    :param handle: Handle of user to get.
    :type handle: str

    :rtype: None
    """
    s = [t.text for t in statuses(handle)]
    # Keyword extraction
    r = Rake()
    r.extract_keywords_from_text(" ".join(s))
    return json.dumps(r.get_ranked_phrases())
