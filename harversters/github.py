"""
██╗░░██╗░█████╗░██████╗░██╗░░░██╗██████╗░░██████╗████████╗
██║░░██║██╔══██╗██╔══██╗██║░░░██║╚════██╗██╔════╝╚══██╔══╝
███████║███████║██████╔╝╚██╗░██╔╝░█████╔╝╚█████╗░░░░██║░░░
██╔══██║██╔══██║██╔══██╗░╚████╔╝░░╚═══██╗░╚═══██╗░░░██║░░░
██║░░██║██║░░██║██║░░██║░░╚██╔╝░░██████╔╝██████╔╝░░░██║░░░
╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░╚═════╝░╚═════╝░░░░╚═╝░░░

370rokas (c) 2022
https://github.com/370rokas

harvesters/github.py - Harvests info from GitHub
"""

import requests


def dig_username(username):
    data = {}

    def add(i, v):
        data[i] = v

    resp = requests.get(f'https://api.github.com/users/{username}')
    if resp.status_code != 200:
        return {}

    resp_data = resp.json()

    add("Username", resp_data["login"])
    add("Name", resp_data["name"])
    add("Email", resp_data["email"])
    add("Bio", resp_data["bio"])
    add("Blog", resp_data["blog"])
    add("Twitter", resp_data["twitter_username"])
    add("Hireable", resp_data["hireable"])
    add("Location", resp_data["location"])
    add("AvatarURL", resp_data["avatar_url"])
    add("Company", resp_data["company"])
    add("PublicRepos", resp_data["public_repos"])
    add("Followers", resp_data["followers"])
    add("Following", resp_data["following"])
    add("CreationDate", resp_data["created_at"])
    add("UpdateDate", resp_data["updated_at"])

    # TODO : Get all Organizations and Repos (organizations_url, repos_url)

    return data


def run_username(username):
    res = {}

    resp = requests.get(f'https://api.github.com/users/{username}')
    if resp.status_code != 200:
        res["Found"] = False
        res["Url"] = ""
        res["Data"] = {}
    else:
        res["Found"] = True
        res["Url"] = f'https://github.com/{username}'
        res["Data"] = dig_username(username)

    return res


def run_email(email):
    print("")
    # TODO : Search GH by Email
