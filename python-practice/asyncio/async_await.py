import asyncio

async def main():
    print('hello')
    await asyncio.sleep(1)
    print('world')

main()

# await main() # error: await can be used inside async