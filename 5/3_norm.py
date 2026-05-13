"№ 28926 ЕГКР 18.04.26 (Уровень: Базовый)"

def f3(x):
    s = ''
    while x:
        s += str(x % 3)
        x = x // 3
    return s[::-1]

for n in range(1, 100):
    f3_n = f3(n)
    if n % 3 == 0:
        f3_n = f3_n + f3_n[-2:]
    else:
        f3_n = f3_n + f3(sum(map(int, f3_n)) * 2)
    r = int(f3_n, 3)
    if r > 520 and r % 2 != 0:
        print(r)

# Next, we go to Libro Office Calc and use the minimum column search function and get the answer.
# 567