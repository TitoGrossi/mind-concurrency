import asyncio
from random import randint
from typing import List

async def generate_value() -> int:
    return randint(1, 2)

async def retrieve_data() -> int:
    random_value = randint(1, 2)
    await asyncio.sleep(random_value)
    return random_value

async def main():
    data_retrieved: List[int] = []

    for _ in range(10):
        data = await retrieve_data()
        data_retrieved.append(data)
        
    print(data_retrieved)

if __name__ == "__main__":
    asyncio.run(main())
