# %%
import csv

import requests


# %%
def main():
    for page in range(1, 16):
        data = get_data(page)
        if page == 1:
            keys = data[0].keys()

        write(keys, data, str(page))


def get_data(page):
    return requests.get(
        "http://api.linode.com/v4/linode/stackscripts?page=" + str(page)
    ).json()["data"]


def write(keys, rows, filename):
    with open("stackscripts/{}.csv".format(filename), "w") as output_file:
        writer = csv.DictWriter(output_file, keys)
        writer.writeheader()
        writer.writerows(rows)


# %%
if __name__ == "__main__":
    main()
