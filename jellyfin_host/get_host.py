import asyncio
import os

import httpx
base_dir = os.path.dirname(__file__)
file_path = os.path.join(base_dir, "host.ini")

async def main():
    async with httpx.AsyncClient() as client:
        results = []
        s = []
        for i in urls:
            resp = await client.get(f'https://dns.google/resolve?name={i}&type=A')
            results.append(resp.json())
        for item in results:
            for ans in item["Answer"]:
                s.append(f"      - {ans['name'].strip('.')}:{ans['data']}\n")
    with open(file_path, "w") as f:
        f.writelines(s)







if __name__ == '__main__':
    urls = [
        "image.tmdb.org",
        "api.themoviedb.org",
        "www.themoviedb.org",
        "www.omdbapi.com",
        "img.omdbapi.com",
        "www.thetvdb.com",
        "api.thetvdb.com",
        "api.opensubtitles.com"
    ]
    asyncio.run(main())
