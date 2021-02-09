import asyncio
import json
import threading
import time, requests
from pprint import pformat, pprint
from bs4 import BeautifulSoup


# get slugs
def getSlugs():
    coins = {}
    for i in range(0, 41):
        if i == 0:
            i = ""
        else:
            i = f"{i}/"
        url = f"https://coinmarketcap.com/{i}"
        before = time.time()
        page = requests.get(url)
        print(f"Recieved page {url} in {time.time()-before:.2f}s")
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
    with open("data.json", "w+") as outfile:
        json.dump((coins), outfile)
    pprint(coins)


if __name__ == "__main__":
    getSlugs()