"№ 1520 (Уровень: Средний)"

for a in range(2):
    for b in range(2):
        for c in range(2):
            f = a and (not b) or c
            if f == 0:
                print(b, c, a, '|', f * 1)
# bca
