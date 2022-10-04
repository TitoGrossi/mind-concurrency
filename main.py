from random import randint
from time import sleep
from typing import List

def retrieve_data() -> int:
    random_value = randint(1, 2)
    sleep(random_value)
    return random_value

def main():
    data_retrieved: List[int] = []

    for _ in range(10):
        data = retrieve_data()
        data_retrieved.append(data)
    
    print(data_retrieved)

if __name__ == "__main__":
    main()
