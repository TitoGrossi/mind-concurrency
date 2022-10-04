from random import randint
import asyncio


async def retrieve_data() -> int:
    random_value = randint(1, 2)
    await asyncio.sleep(1)
    return random_value

async def main():
    data_retrieved = await asyncio.gather(
        *[retrieve_data() for _ in range(10)]
    )
    print(data_retrieved)

if __name__ == "__main__":
    asyncio.run(main())
