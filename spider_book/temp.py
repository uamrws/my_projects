import asyncio

import httpx

HEADERS = {
    "Proxy-Connection": "keep-alive",
    "Cache-Control": "max-age=0",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8"
}


async def download(url):
    pass


async def main():
    with open("book_info.tsv") as f:
        books = f.readlines()[1:]

    # books.sort(key=lambda x: int(x.split()[4]), reverse=True)
    for i in books:
        try:
            int(i.split()[4])
        except:

            print(i.split(), end="\n")

    # async with httpx.AsyncClient(headers=HEADERS, timeout=None) as client:
    #     resp = await client.get("http://185.163.45.196/23/wbygjy,qyjx.rar")
    #
    #     with open("temp.rar", 'wb') as f:
    #         f.write(resp.read())


if __name__ == '__main__':
    asyncio.run(main())
