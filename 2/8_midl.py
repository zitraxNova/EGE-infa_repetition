"№ 2534 Статград 27.10.2021 (Уровень: Средний)"

for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = (x == (not y)) <= ((x and w) == (z and (not w)))
                if f == 0:
                    print(w, z, y, x, '|', f * 1)
# wzyx