import connexion
from datetime import date, datetime
from typing import List, Dict
from six import iteritems
from ..util import deserialize_date, deserialize_datetime


def influencetags(handle, influencer):
    """
    Determine hashtag similarity between users
    
    :param handle: Handle of user to get.
    :type handle: str
    :param influencer: Handle of user to examine influence from.
    :type influencer: str

    :rtype: None
    """
    return 'do some magic!'


def influencetags_0(handle, influencer):
    """
    Determine mention similarity between users
    
    :param handle: Handle of user to get.
    :type handle: str
    :param influencer: Handle of user to examine influence from.
    :type influencer: str

    :rtype: None
    """
    return 'do some magic!'


def influencetime(handle, influencer):
    """
    determines how close users tweet to each other
    
    :param handle: Handle of user to get.
    :type handle: str
    :param influencer: Handle of user to examine influence from.
    :type influencer: str

    :rtype: None
    """
    return 'do some magic!'


def influencetopic(handle, influencer):
    """
    Determine topic similarity between users
    
    :param handle: Handle of user to get.
    :type handle: str
    :param influencer: Handle of user to examine influence from.
    :type influencer: str

    :rtype: None
    """
    return 'do some magic!'


def usermentions(handle):
    """
    Get users which a user has mentioned
    
    :param handle: Handle of user to get.
    :type handle: str

    :rtype: None
    """
    return 'do some magic!'


def useroverview(handle):
    """
    Get basic information about a user
    
    :param handle: Handle of user to get.
    :type handle: str

    :rtype: None
    """
    return 'do some magic!'


def usertags(handle):
    """
    Get most common recent hashtags used by a user
    
    :param handle: Handle of user to get.
    :type handle: str

    :rtype: None
    """
    return 'do some magic!'


def usertimes(handle):
    """
    Gets a picture of when a user tweets
    
    :param handle: Handle of user to get.
    :type handle: str

    :rtype: None
    """
    return 'do some magic!'


def usertopics(handle):
    """
    Gets topics a user uses, grouped using word2vec
    
    :param handle: Handle of user to get.
    :type handle: str

    :rtype: None
    """
    return 'do some magic!'
