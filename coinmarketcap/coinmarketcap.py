import asyncio
import json
import threading
import time, requests
from pprint import pformat, pprint
from bs4 import BeautifulSoup

_BASE = "https://coinmarketcap.com"
SLUGS = {}

__author__ = "Calvin Kinateder"
__email__ = "calvinkinateder@gmail.com"

# get slugs
def fetchSlugs(filename=None, loud=False):
    """
    Get slugs from coinmarketcap and return a dictionary of form.
    Will save to filename as well.
    {
        "symbol": "slug",
    }
    """
    coins = {}
    for i in range(0, 41):
        if i == 0:
            i = ""
        else:
            i = f"{i}/"
        url = f"{_BASE}/{i}"

        # load page and time
        before = time.time()
        page = requests.get(url)
        if loud:
            print(f"Recieved page {url} in {time.time()-before:.2f}s")

        # parse and search for required data
        parsed = BeautifulSoup(page.content, "html.parser")
        data = parsed.find("script", id="__NEXT_DATA__", type="application/json")
        coin_data = json.loads(data.contents[0])
        listings = coin_data["props"]["initialState"]["cryptocurrency"][
            "listingLatest"
        ]["data"]
        # pprint(listings)
        for i in listings:
            coins[str(i["symbol"])] = i["slug"]
    # save slugs
    if filename:
        with open(filename.strip() + ".json", "w+") as outfile:
            json.dump((coins), outfile)
    globals()["SLUGS"] = coins
    return coins


def loadSlugs(filename):
    """
    Load slugs from a json file [filename].
    """
    with open(
        filename.strip().replace(".json", "") + ".json"
    ) as f:  # replacing json incase its passed twice
        globals()["SLUGS"] = json.load(f)
    return globals()["SLUGS"]


def __fetchSingleSymbol(symbol):
    if symbol in SLUGS:
        slug = SLUGS[symbol]
        print(slug)
    else:
        return False


def fetchSymbols(symbols):
    if type(symbols) == str:  # single
        pass
    elif type(symbols) == list:  # multiple
        pass


if __name__ == "__main__":
    loadSlugs("slugs")
    pprint(SLUGS)