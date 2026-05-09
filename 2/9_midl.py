"№ 5057 (Уровень: Средний)"

for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = (w <= (y == z)) and (y == (z == x))
                if f == 1:
                    print(z, w, y, x, '|', f * 1)
# zwyx