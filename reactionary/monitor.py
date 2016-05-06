
"""
reactionary.monitor
~~~~~~~~~~~~~~~~~~~

Monitoring code for reactionary

"""

import praw
import pdb
import re
import os

# external class which does the bulk of the work
from .user import User

# get reddit_username and reddit_password from local file login_details.py
from .credentials import *
from .config import get_config


def monitor():
    cfg = get_config()
    r = reddit_login(creds, cfg['credentials']['useragent'])
    # TODO: this should be oauth based
    # r.login(reddit_username, reddit_password)

    # create an array with a list of submission ids already processed
    # in the past
    # posts_scanned.txt is a local text file containing a list of ids
    # TODO: need to check the file is present
    with open(cfg['data']['posts_scanned'], "r") as f:
        posts_scanned = f.read()
        posts_scanned = posts_scanned.split("\n")
        posts_scanned = filter(None, posts_scanned)

    # change this to determine which subs the bot will monitor
    # TODO: subs should be set by config
    subreddit = r.get_subreddit('anarchism+metanarchism')

    # edit this to change subs being considered reactionary
    # subs that are automatically monitored
    # TODO: subs should be set by config
    suspicious_subs = ["mensrights", "theredpill", "coontown",
                       "greatapes", "whiterights", "protectandserve",
                       "darkenlightenment", "gendercritical", "gender_critical",
                       "fatpeoplehate", "fatlogic", "new_right",
                       "nationalsocialism", "nazi", "european",
                       "polistan", "antipoz", "monarchism",
                       "hbd", "srssucks", "sjsucks", "pissbeuponhim",
                       "sjwhate", "strugglefucking", "rapingwomen",
                       "killingwomen", "beatingwomen2", "beatingcripples",
                       "beatingniggers", "beatingtrannies", "trans_fags"]

    # get newest 50 submissions on r@ and met@
    for submission in subreddit.get_new(limit=50):
        # if this is the first time the bot ever sees this submission
        if submission.id not in posts_scanned:
            # get username of submitter
            username = submission.author.name

            user = User(username, r, suspicious_subs, 50)
            user.process_comments()
            user.process_submitted()

            info = user.get_monitoring_info()

            if len(info) > 0:
                info += "\n\n___\n\n^I'm ^a ^bot. ^Only ^the ^past ^1,000 ^comments ^are ^fetched."
                info.replace("http://www.", "http://np.")
                info = info[:10000]
                submission.add_comment(info)

            posts_scanned.append(submission.id)

            with open(cfg['data']['posts_scanned'], "w") as f:
                for post_id in posts_scanned:
                    f.write(post_id + "\n")
