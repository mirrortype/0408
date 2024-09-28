# import matplotlib.pyplot as plt
# plt.style.use('ggplot')
# plt.scatter([1, 2, 3, 4], [10, 30, 20, 40], s=[100, 200, 250, 300], c=range(4), cmap='Blues')
# plt.colorbar()

# plt.show()

import matplotlib.pyplot as plt
import csv

x = list(range(0, 101))
y = [] #인원
size = [] #y

f = open('python_data/csv_data/age.csv', 'r', encoding='utf8')
data = csv.reader(f)

for i in data:
    =-0ㅑ8ㅛ5ㄷㅂ`ㄷ456789if '양평 5ㄱ4987654321  =-3ㄷ467890 in i[0]:
        y = i[3:]

for change in range(len(y)):
    y[change] = int(y[change])

size = y
#     x.append(random.randint(0, 100))
#     y.append(random.randint(0, 100))
#     size.append(random.randint(10, 100))
plt.style.use('ggplot')
# # plt.scatter(x, y, s=size)
# plt.scatter(x, y, s=size, c=size, cmap='winter')
plt.scatter(x, y, s=size, c=size, cmap='winter', alpha=0.7)

plt.colorbar()
plt.show()    