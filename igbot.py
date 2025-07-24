import argparse
import json
import pandas as pd


def process_user(user: str) -> None:

    # Loads relevant files
    try:
        with open(f"./{user}/followers_1.json") as file:
            followers = json.load(file)
    except:
        raise FileNotFoundError(f"The file ./{user}/followers_1.json does not exist")

    try:
        with open(f"./{user}/following.json") as file:
            following = json.load(file)
    except:
        raise FileNotFoundError(f"The file ./{user}/following.json does not exist")

    # Parses following and followers
    try:
        following = [
            user["string_list_data"][0]["value"]
            for user in following["relationships_following"]
        ]
        followers = [user["string_list_data"][0]["value"] for user in followers]
    except:
        raise Exception("Failed to parse following and followers")

    # Computes differences
    dont_follow_you = sorted(set(following) - set(followers))
    you_dont_follow = sorted(set(followers) - set(following))

    # Pads length
    max_len = max(len(dont_follow_you), len(you_dont_follow))
    dont_follow_you += [None] * (max_len - len(dont_follow_you))
    you_dont_follow += [None] * (max_len - len(you_dont_follow))

    # Saves as df
    df = pd.DataFrame(
        {
            "Don't Follow You": dont_follow_you,
            "You Don't Follow": you_dont_follow,
        }
    )

    # Saves differences to CSV
    path = f"./{user}/{user}_users.csv"
    df.to_csv(path, index=False)
    print("Saved one-way instagram connections to", path)


if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    # User
    parser.add_argument(
        "-u", "--user", type=str, required=True, help="The user to process."
    )

    args = parser.parse_args()

    # Processes the user
    process_user(user=args.user)
