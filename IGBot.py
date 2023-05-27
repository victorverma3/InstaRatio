#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 25 17:26:25 2023

@author: victor
"""
import json
import pandas as pd
import time

# run the file for instructions
print("\nInstructions:")
print("1. Open Instagram -> Settings -> Privacy and Security")
print("2. Request data download as json files")
print("3. Move followers_1.json and following.json into a folder called <user> in the same directory as this file\n")
print("When ready, type in: go(user)")
print("If you want to get results instantly, type in: go(user, 'f')\n")
print("<user> should be a lowercase string representing the person whose data is being used")

# check which users don't follow you back
def go(user, speed = None):
    # open relevant files
    with open(f'./{user}/followers_1.json') as file:
        followers = json.load(file)
    with open(f'./{user}/following.json') as file:
        following = json.load(file)
    
    # create list of people who don't follow user back
    following_list = []
    for following in following['relationships_following']:
        following_list.append(following["string_list_data"][0]["value"])
    for follower in followers:
        if follower["string_list_data"][0]["value"] in following_list:
            following_list.remove(follower["string_list_data"][0]["value"])
    
    # format results
    following_list.sort()
    
    # creates a csv containg the users
    data = {
        'Users': following_list
        }
    df = pd.DataFrame(data, columns = ['Users'])
    path = f'./{user}/{user}users.csv'
    df.to_csv(path, index = 'False')
    
    # display results
    if speed != 'f':
        print("\nThe following users don't follow you back on instagram:\n")
        for user in following_list:
            print(user)
            time.sleep(0.125)
    print(f"\n{str(len(following_list))} users don't follow you back")
    return following_list