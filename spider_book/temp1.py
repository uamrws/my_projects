import asyncio


async def main():
    proc = await asyncio.create_subprocess_shell(
        "unrar x temp.rar",
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )



if __name__ == '__main__':
    asyncio.run(main())
