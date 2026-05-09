"№ 22073 (Уровень: Базовый)"
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = (z <= y) or ((w <= x) <= y)
                if f == 0:
                    print(y, w, x, z, '|', f * 1)
# ywxz