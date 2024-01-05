import json
import pandas as pd


def find(user):
    # open relevant files
    with open(f"./{user}/followers_1.json") as file:
        followers = json.load(file)
    with open(f"./{user}/following.json") as file:
        following = json.load(file)

    # finds fakes and fans
    following = [
        user["string_list_data"][0]["value"]
        for user in following["relationships_following"]
    ]
    followers = [user["string_list_data"][0]["value"] for user in followers]

    fakes = list(set(following) - set(followers))
    fans = list(set(followers) - set(following))

    # sorts results
    fakes.sort()
    fans.sort()

    # creates a csv containing the users
    data = {"Don't Follow You": fakes}
    df = pd.DataFrame(data, columns=["Don't Follow You"])
    newSeries = pd.Series(fans, name="You Don't Follow")
    df = pd.concat([df, newSeries], axis=1)
    path = f"./{user}/{user}users.csv"
    df.to_csv(path, index="False")
    print(
        f"\nThe list of fakes and fans is available in csv format at ./{user}/{user}users.csv\n"
    )
    return df
