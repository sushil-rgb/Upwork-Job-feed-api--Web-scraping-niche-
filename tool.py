from fake_useragent import UserAgent
# from datetime import datetime
import itertools
import aiohttp
# import tzlocal
# import pytz


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


# def timezone_conversion(str_time):
#     time = datetime.strptime(str_time, "%H:%M:%S")
#     time_utc = pytz.utc.localize(time)
#     local_timezone = tzlocal.get_localzone()
#     time_local = time_utc.astimezone(local_timezone)
#     return time_local.time()


def filter(raw_lists):
    filtered_lists = []
    for file in raw_lists:
        if not file in filtered_lists:
            filtered_lists.append(file)
    return filtered_lists


def remove_duplicates(data):
    seen = set()
    unique_data = []
    for item in data:
        key = (item['title'], item['link'], item['post_date'], item['post_time'])
        if key not in seen:
            unique_data.append(item)
            seen.add(key)
    sorted_jobs = sorted(unique_data, key=lambda x: (x['post_date'], x['post_time']), reverse = False)
    return sorted_jobs


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

