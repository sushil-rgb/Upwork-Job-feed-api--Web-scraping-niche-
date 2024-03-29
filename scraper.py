from bs4 import BeautifulSoup
from datetime import datetime
from tool import Response


async def job_alerts():
    job_datas = []
    for page in range(0, 20, 10):
        rss_url = f"https://www.upwork.com/ab/feed/jobs/rss?paging={page}%3B10&q=data+extraction+web+scraping+data+scraping&sort=recency&subcategory2_uid=531770282593251331&api_params=1&securityToken=9036a5d7ac251defd2cbbdb953be6517dccc8dc88a16442dbe27b213db19c07588315c71fa8e894087e88e44384a7743bf0a75944eecda66f0909750157b2e4d&userUid=1368080374926864384&orgUid=1368080374926864385"
        cont = await Response(rss_url).content()
        soup = BeautifulSoup(cont, 'xml')
        jobs = soup.select('channel')
        for job in jobs:
            for idx in range(10):
                datas = {
                    'title': [j.text.strip() for j in job.select('title')[2:]][idx],
                    'link': [j.text.strip() for j in job.select('link')[2:]][idx],
                    'post_time': [datetime.strptime(j.text.strip(), "%a, %d %b %Y %H:%M:%S %z") for j in job.select('pubDate')][idx]

                }
                job_datas.append(datas)

    return job_datas

