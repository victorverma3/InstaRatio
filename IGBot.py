#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 17:26:25 2023

@author: victor
"""
import json
import pandas as pd

# run the file for instructions
print("\nInstructions:")
print("1. Open Instagram -> Settings -> Privacy and Security")
print("2. Request data download as json files")
print("3. Move followers_1.json and following.json into a folder called {user} in the same directory as this file\n")
print("When ready, type in: find(user)")
print("{user} should be a lowercase string representing the person whose data is being used")

# program
def find(user):
    # open relevant files
    with open(f'./{user}/followers_1.json') as file:
        followers = json.load(file)
    with open(f'./{user}/following.json') as file:
        following = json.load(file)
    
    # finds fakes and fans
    following = [user['string_list_data'][0]['value'] for user in following['relationships_following']]
    followers = [user['string_list_data'][0]["value"] for user in followers]
    
    fakes = list(set(following) - set(followers))
    fans = list(set(followers) - set(following))
    
    # sorts results
    fakes.sort()
    fans.sort()
    
    # creates a csv containing the users
    data = {
        "Fakes": fakes
        }
    df = pd.DataFrame(data, columns = ["Fakes"])
    newSeries = pd.Series(fans, name = 'Fans')
    df = pd.concat([df, newSeries], axis = 1)
    path = f'./{user}/{user}users.csv'
    df.to_csv(path, index = 'False')
    print(f'\nThe list of fakes and fans is available in csv format at ./{user}/{user}users.csv\n')
    return df