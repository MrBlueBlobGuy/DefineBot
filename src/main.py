import praw


import getconfig

reddit = praw.Reddit(
    user_agent = getconfig.user_agent,
    client_id = getconfig.client_id,
    client_secret = getconfig.client_secret
)

print(reddit)
input()