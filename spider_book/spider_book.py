import asyncio
import logging as log
import random
import re

import httpx
from lxml import etree

log.basicConfig(format='%(message)s', level='INFO')
HEADERS = {
    "Proxy-Connection": "keep-alive",
    "Cache-Control": "max-age=0",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8"
}


async def get_bset_worst(client, url):
    resp = await client.get(url)
    if resp.status_code == 200:
        content = resp.text
        if content:
            best_ = content.split(',')[0]
            worst_ = content.split(',')[-1]
        else:
            best_ = 0
            worst_ = 0
        return best_, worst_
    else:
        await asyncio.sleep(random.uniform(1, 3) * 3)
        return await get_bset_worst(client, url)


async def get_book_info(client, baseurl, book_type, book_name, book_author):
    log.info(f'获取{book_type}频道{book_name}信息')
    down_id = baseurl.split('/')[-1]
    url = f"http://www.zxcs.me/content/plugins/cgz_xinqing/cgz_xinqing_action.php?action=show&id={down_id}"
    best_, worst_ = await get_bset_worst(client, url)

    url = f"http://www.zxcs.me/download.php?id={down_id}"
    resp = await client.get(url)
    if resp.status_code == 200:
        html = etree.HTML(resp.text)
        content = html.xpath("//span[@class='downfile']/a")
        url_list = ' ， '.join([i.get('href') for i in content])
        with open('book_info.tsv', 'a') as f:
            f.write('\t'.join([
                down_id, book_name, book_author, book_type,
                best_, worst_, url_list
            ]) + '\n')
    else:
        await asyncio.sleep(random.uniform(1, 3) * 3)
        await get_book_info(client, baseurl, book_type, book_name, book_author)


async def handle_book(client, url, book_type, book_name, book_author):
    await asyncio.sleep(random.uniform(1, 3) * 3)
    resp = await client.get(url)
    if resp.status_code == 200:
        await get_book_info(client, url, book_type, book_name, book_author)
    else:
        await asyncio.sleep(random.uniform(1, 3) * 3)
        await handle_book(client, url, book_type, book_name, book_author)


async def handle_response(client, url, title, page=1):
    log.info(f'获取{title}频道第{page}页书本url')
    await asyncio.sleep(random.uniform(1, 3) * 3)
    resp = await client.get(url + f'/page/{page}')
    if resp.status_code == 200:
        html = etree.HTML(resp.text)
        content = html.xpath("//dl/dt[1]/a")

        cors = []
        for i in content:
            info = re.split(r'（.*）', i.text)
            book_type = title
            book_name, book_author = info
            cors.append(
                handle_book(client, i.get('href'), book_type, book_name, book_author)
            )
        await asyncio.gather(*cors)

        last_page = html.xpath("//div[@id='pagenavi']/*[position()>last()-3]/text()")
        if last_page:
            '»' in last_page and last_page.remove('»')
            '...' in last_page and last_page.remove('...')
        if not last_page or int(last_page.pop()) > page:
            page += 1
            await handle_response(client, url, title, page=page)
    else:
        await asyncio.sleep(random.uniform(1, 3) * 3)
        await handle_response(client, url, title, page=page)


async def get_menu(client):
    log.info('获取所有频道url...')
    resp = await client.get('http://zxcs.me/?security_verify_data=313434302c393030')
    print(resp)
    if resp.status_code == 301:
        resp = await client.get('http://zxcs.me/')
        print(resp)
    if resp.status_code == 200:
        html = etree.HTML(resp.text)
        content = html.xpath("//ul[@id='topmenu']/li[position()>1]/a")
        print(content)
        cors = [
            handle_response(client, i.get('href'), i[0].text)
            for i in content
        ]
        await asyncio.gather(*cors)
    else:
        await get_menu(client)


async def main():
    async with httpx.AsyncClient(headers=HEADERS, timeout=None) as client:
        await get_menu(client)


if __name__ == '__main__':
    asyncio.run(main())
