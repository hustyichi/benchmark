# copy by https://github.com/secretflow/spu/blob/main/libspu/psi/tools/generate_psi.py
from random import randint
from random import sample
import csv
import sys


def random_with_N_digits(n):
    range_start = 10 ** (n - 1)
    range_end = (10**n) - 1
    return randint(range_start, range_end)


row_list = []
len1 = 10**2
len2 = 10
len3 = 10
len4 = 10

if len(sys.argv) > 1:
    len1 = int(sys.argv[1])
    len2 = int(len1 / 2)

if len(sys.argv) > 2:
    len3 = int(sys.argv[2])

len4 = int(len3 / 2)
print(len1, len2)


for i in range(len1):
    data_list = [random_with_N_digits(8), random_with_N_digits(2), random_with_N_digits(2)]
    row_list.append(data_list)

row_list2 = sample(row_list, len2)
for i in range(len2, len1):
    data_list = [random_with_N_digits(8), random_with_N_digits(2), random_with_N_digits(2)]
    row_list2.append(data_list)

row_list3 = sample(row_list, len4)
for i in range(len4, len3):
    data_list = [random_with_N_digits(8), random_with_N_digits(2), random_with_N_digits(2)]
    row_list3.append(data_list)

print(len(row_list2))
print(len(row_list3))

with open(f'pearson_{len1}_1.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["id", "y", "x"])
    writer.writerows(row_list)

with open(f'pearson_{len1}_2.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["id", "y", "x"])
    writer.writerows(row_list2)

with open(f'pearson_{len1}_3.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["id", "y", "x"])
    writer.writerows(row_list3)
