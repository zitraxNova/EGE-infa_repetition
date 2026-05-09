"№ 5483 (Уровень: Средний)"

for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = (z == (not x)) <= ((w <= (not y)) and (y <= x))
                if f == 1:
                    print(y, z, x, w, '|', f * 1)
# yzxw