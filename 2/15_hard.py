"№ 567 Джобс 26.10.2020 (Уровень: Средний)"

for a in range(2):
    for b in range(2):
        for c in range(2):
            f = a == (b <= c)
            if f == 1:
                print(b, c, a, '|', f * 1)
# bca