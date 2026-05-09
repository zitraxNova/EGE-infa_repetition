"№ 5867 Danov 2301 (Уровень: Средний)"

for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = (w == (z <= x)) and y
                if f == 0:
                    print(y, w, z, x, '|', f * 1)
# ywzx