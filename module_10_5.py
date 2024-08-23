from multiprocessing import Pool
from datetime import datetime


def read_info(name):
    all_data = []
    with open(name, 'r') as f:
        while True:
            line = f.readline()
            all_data.append(line)
            if not line:
                break


files = [f'./file {number}.txt' for number in range(1, 5)]

start_time = datetime.now()
for file_name in files:
    read_info(file_name)
end_time = datetime.now()
print(f'Линейный вызов: {end_time - start_time}')

# Линейный вызов: 0:00:04.559782

if __name__ == '__main__':
    with Pool(4) as p:
        start_time = datetime.now()
        p.map(read_info, files)
        end_time = datetime.now()
    print(f'Многопроцессорный вызов: {end_time - start_time}')

# Многопроцессорный вызов: 0:00:01.636122
