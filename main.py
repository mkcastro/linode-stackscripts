# %%
import json

import requests


# %%
def main():
    container = []
    for page in range(1, 16):
        container.extend(get_data(page))

    write(container)


def get_data(page):
    return requests.get(
        "http://api.linode.com/v4/linode/stackscripts?page={}".format(page)
    ).json()["data"]


def write(data):
    with open("output.json", "w") as outfile:
        json.dump(data, outfile)


if __name__ == "__main__":
    main()
