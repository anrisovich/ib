"""
    Whitelist generator: generates a list of users which
    will not be unfollowed.
"""

import sys
import os
import time
import random

sys.path.append(os.path.join(sys.path[0], '../../'))
from instabot import Bot

bot = Bot()
bot.login()

wait = 4

your_following = bot.get_user_following(bot.user_id)
already_whitelisted = bot.read_list_from_file("whitelist.txt")
rest_users = list(set(your_following) - set(already_whitelisted))
random.shuffle(rest_users)
with open("whitelist.txt", "a") as f:
    for user_id in rest_users:
        user_info = bot.get_user_info(user_id)
        print(user_info["username"])

        input_line = "y"
        if "y" in input_line:
            f.write(str(user_id) + "\n")
            print("ADDED.\r")
        time.sleep(wait)
