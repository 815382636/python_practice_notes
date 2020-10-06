# 协程是实现并发编程的一种方式。

import asyncio
import random
from time import time


async def crawl_page(url):
    print('crawling {}'.format(url))
    sleep_time = int(url.split('_')[-1])
    await asyncio.sleep(sleep_time)
    print('OK {}'.format(url))


async def main1(urls):
    tasks = [asyncio.create_task(crawl_page(url)) for url in urls]
    await asyncio.gather(*tasks)
    # for task in tasks:
    #     await task


# time1 = time()
# print(asyncio.run(main1(['url_1', 'url_2', 'url_3', 'url_4'])))
# time2 = time()
# print(f"花费的时间：{time2-time1}")


# 生产者消费者模式


async def consumer(queue, id):
    while True:
        val = await queue.get()
        print('{} get a val: {}'.format(id, val))
        await asyncio.sleep(1)


async def producer(queue, id):
    for i in range(5):
        val = random.randint(1, 10)
        await queue.put(val)
        print('{} put a val: {}'.format(id, val))
        await asyncio.sleep(1)


async def main():
    queue = asyncio.Queue()

    consumer_1 = asyncio.create_task(consumer(queue, 'consumer_1'))
    consumer_2 = asyncio.create_task(consumer(queue, 'consumer_2'))

    producer_1 = asyncio.create_task(producer(queue, 'producer_1'))
    producer_2 = asyncio.create_task(producer(queue, 'producer_2'))

    await asyncio.sleep(10)
    consumer_1.cancel()
    consumer_2.cancel()

    await asyncio.gather(consumer_1, consumer_2, producer_1, producer_2, return_exceptions=True)


# time1 = time()
# print(asyncio.run(main()), end="\t")
# time2 = time()
# print(f"花费的时间：{time2-time1}")

# 豆瓣爬虫

import requests
from bs4 import BeautifulSoup

import asyncio
import aiohttp

from bs4 import BeautifulSoup


async def fetch_content(url):
    async with aiohttp.ClientSession(
            connector=aiohttp.TCPConnector(ssl=False)
    ) as session:
        async with session.get(url) as response:
            return await response.text()


async def main():
    url = "https://movie.douban.com/cinema/later/beijing/"
    init_page = await fetch_content(url)
    init_soup = BeautifulSoup(init_page, 'lxml')

    movie_names, urls_to_fetch, movie_dates = [], [], []

    all_movies = init_soup.find('div', id="showing-soon")
    for each_movie in all_movies.find_all('div', class_="item"):
        all_a_tag = each_movie.find_all('a')
        all_li_tag = each_movie.find_all('li')

        movie_names.append(all_a_tag[1].text)
        urls_to_fetch.append(all_a_tag[1]['href'])
        movie_dates.append(all_li_tag[0].text)

    tasks = [fetch_content(url) for url in urls_to_fetch]
    print(f"-------{urls_to_fetch}-----------------")
    pages = await asyncio.gather(*tasks)

    for movie_name, movie_date, page in zip(movie_names, movie_dates, pages):
        soup_item = BeautifulSoup(page, 'lxml')
        img_tag = soup_item.find('img')

        print('{} {} {}'.format(movie_name, movie_date, img_tag['src']))


asyncio.run(main())
