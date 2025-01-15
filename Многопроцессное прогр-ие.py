import time
from multiprocessing import Pool

def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as file:
        for line in file:
            all_data.append(line)
    #return all_data

if __name__ == '__main__':
    filenames = [f'./file {number}.txt' for number in range(1, 5)]

    start = time.time()
    over = time.time()
    time_1 = over - start
    start_2 = time.time()
    print(f'Линейный вызов: {time_1}')

    with Pool(processes=4) as pool:
        pool.map(read_info, filenames)
    over_2 = time.time()
    time_2 = over_2 - start_2
    print(f'Многопроцессный вызов: {time_2}')
