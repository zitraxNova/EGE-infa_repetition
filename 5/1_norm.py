"№ 27617 Апробация 04.03.26 (Уровень: Базовый)"

for n in range(1, 100):
    bin_n = bin(n)[2:]
    if n % 3 == 0:
        bin_n = bin_n + bin_n[-3:]
    else:
        res = n % 3 * 3
        bin_n = bin_n + bin(res)[2:]
    r = int(bin_n, 2)
    if 120 <= r <= 140:
        print(n, r)
