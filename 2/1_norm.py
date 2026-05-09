" № 29334 Открытый вариант 2026 (Уровень: Базовый) "

for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = ((z <= x) <= (x == y)) or (not w)
                if f == 0:
                    print(y, x, w, z, '|', f * 1)
# yxwz