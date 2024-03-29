from fake_useragent import UserAgent
from urllib.parse import urlparse
import itertools
import aiohttp


class Response:
    def __init__(self, base_url):
        self.base_url = base_url

    async def content(self):
        async with aiohttp.ClientSession() as session:
            headers = {'User-Agent': userAgents()}
            async with session.get(self.base_url, headers = headers) as resp:
                cont = await resp.read()
                return cont

    async def response(self):
        async with aiohttp.ClientSession() as session:
            headers = {'User-Agent': userAgents()}
            async with session.get(self.base_url, headers = headers) as resp:
                cont = resp.status
                return cont


def filter_duplicates(raw_lists):
    filtered_lists = []

    # Iterate through each element in the input list:
    for file in raw_lists:

        # Check if the element is not already in the filtered list:
        if not file in filtered_lists:

            # Append the element to the filtered list:
            filtered_lists.append(file)
    return filtered_lists


def flat(d_lists):
    """
    Flatten a multi-dimentional list.

    Args:
    - d_lists (list): A multi-dimensional list.

    Returns:
    - list: A flattened version of the input list.
    """
    # Use itertools.chain to flatten the multi-dimensional list
    return list(itertools.chain(*d_lists))


def userAgents():
    """
    Returns a random user agent string from a file containing a list of user agents.

    Args:
        -None

    Returns:
        -A string representing a ranom user agent.
    """
    agents = UserAgent()
    return agents.random

