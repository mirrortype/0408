import random


def sorting(length):
    n = []

    num = 0
    while len(n) < length:
        num = random.randint(1, 1000)
        if num in n:
            continue
        else:
            n.append(num)
    print(n)

    shift = 0
    count = 0
    while True:
        shift = 0 
        for i in range(len(n) - 1):
            if n[i] < n[i + 1]:
               n[i], n[i + 1] = n[i + 1], n[i]
               shift += 1
               count += 1
        if shift == 0:
            break
    print(n)
    print(f"{count}번 만에 정렬 완료")

number = int(input("몇 개의 숫자를 만드시겠습니까?"))
sorting(number)

