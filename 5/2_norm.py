"№ 27760 Апробация 04.03.26 (Уровень: Базовый)"
for n in range(1,100):
    bin_n = bin(n)[2:]
    if n % 2 == 0:
        bin_n = '10' + bin_n
    else:
        bin_n = '1' + bin_n + '01'
    r = int(bin_n, 2)
    if n > 18:
        print(r)

# Next, we go to Libro Office Calc and use the minimum column search function and get the answer.
# 84