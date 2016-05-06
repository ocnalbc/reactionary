


import praw

from .reactionary import config


def get_credentials():
    pass


def reddit_login(credentials, user_agent):
    r = praw.Reddit(user_agent = user_agent)
    # TODO: this should be oauth based
    r.login(credentials.username, credentials.password)
    return r

def reddit_oath(credentials, user_agent):
    pass
