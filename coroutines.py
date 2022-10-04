from random import randint

# def calculate_new_total() -> int:
#     total = 0
#     new_value = yield
#     total += new_value
#     return total

# isso é uma corotina em python
def averager() -> int:
    total_sum = 0
    number_of_nums = 0
    average = 0

    while True:
        # como na linguagem go, a rotina espera na próxima lina até receber um valor para executar
        # o resto do corpo da função
        new_number = yield
        if new_number is None:
            break
        
        total_sum += new_number
        # total_sum = yield from calculate_new_total()
        number_of_nums += 1
        average = total_sum/number_of_nums
    
    return average

def main():
    coro_avg = averager()
    next(coro_avg)
    for _ in range(10):
        coro_avg.send(randint(0, 100))
    try:
        coro_avg.send(None)
    except StopIteration as exc:
        avg = exc.value

    print(avg)

if __name__ == "__main__":
    main()
