# InstaRatio

A lot of people on Instagram care about their ratio of followers to following,
with a greater follower-following ratio seen as more desirable. This program
identifies accounts that don't follow the user back, as well as accounts that
the user doesn't follow back, to make it easier to optimize the user's
follower-following ratio on Instagram.

## Instructions

1. Open the desired Instagram account download the all-time follower and
   following data as JSON files.
2. After the files are downloaded, create the directory `./<user>`, where `user`
   is the name of the person whose data is being used, and move the files
   `followers_1.json` and `following.json` inside.
3. Activate the venv by running `source venv/bin/activate` in the terminal and
   install the dependencies by running `pip install -r ./requirements.txt` in
   the terminal.
4. Run the command `python3 igbot.py -u <user>` in the terminal, where `user` is
   the name of the person whose data is being used.
5. A CSV with the results will be saved to `./<user>_users.csv`.
