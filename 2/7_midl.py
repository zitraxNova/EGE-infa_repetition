"№ 1888 (Уровень: Средний)"

for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = (not x) or z or (not w) and y
                if f == 0:
                    print(y, x, w, z, '|', f * 1)
# yxwz