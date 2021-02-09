import asyncio
import json
import threading
import time, requests
from pprint import pformat, pprint
from bs4 import BeautifulSoup

_BASE = "https://coinmarketcap.com"
_SLUGS = None

__author__ = "Calvin Kinateder"
__email__ = "calvinkinateder@gmail.com"

# get slugs
def getSlugs(filename=None, loud=False):
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
    globals()["_SLUGS"] = coins
    return coins


if __name__ == "__main__":
    getSlugs()
    pprint(_SLUGS)