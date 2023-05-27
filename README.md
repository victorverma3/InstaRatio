# IGBot

# Inspiration
Most Instagram users are concerned about their following/follower ratio, 
and one of the ways to optimize this ratio is to unfollow accounts who 
don't follow the user back. However, there is no efficient way to do this 
through Instagram, so people have to resort to third-party applications 
and programs that tell them which accounts don't follow the user back. 
There are many other existings programs out there to do this task, but I 
decided to create my own version that is easily accessible to my friends 
and I.

# Setup
First, open the desired Instagram account and navigate to Settings --> 
Privacy and Security. At this screen, request the user data to be 
downloaded as json files. Finally, move the files followers_1.json and 
following.json into a folder called {user}, where user is the name of the 
person whose data is being used. Then, move this folder into the same 
local directory as IGBot.py.

The following python modules must be installed for this program to run: 
json, pandas, and time (see other tutorials online to install these).

Once the setup is complete, run the file IGBot.py and follow the 
instructions that are provided.

