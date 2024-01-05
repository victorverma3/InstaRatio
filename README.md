# InstaRatio

# Overview
A lot of people on Instagram care about their ratio of followers to following, with a greater follower-following ratio seen as more desirable. This program identifies accounts that don't follow the user back, as well as accounts that the user doesn't follow back, to make it easier to optimize the user's follower-following ratio on Instagram.

# Setup
1. Open the desired Instagram account and navigate to `Your activity` --> `Download your information` --> `Request a download` --> `Select accounts and profiles` --> `Select types of information` --> `Followers and following` --> `"JSON" Format` and `"All time" Date range`.
2. After setting these preferences, press `submit request` and download the data from your email when it is completed.
3. Unzip the data and move the files `followers_1.json` and `following.json` into a folder called `user`, where `user` is the name of the person whose data is being used. Then move this folder into the same local directory as `igbot.py`.
4. Run `pip install -r ./requirements.txt` to download the dependencies required to run `igbot.py`.

# Running the program
1. Ensure you have completed the steps in the [Setup](#setup) section.
2. Run `find(user)`, where `user` refers to the folder within the local directory of `igbot.py` that contains the follower and following json files.
3. A CSV file titled `{user}users.csv` will be created within the `user` folder. One column will list accounts that don't follow the user back, and another column will list accounts that the user doesn't follow back.

