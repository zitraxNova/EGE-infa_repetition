"№ 816 Джобс 14.12.2020 (Уровень: Средний)"

for x in range(2):
    for y in range(2):
        for z in range(2):
            f = not(x == (y <= z))
            if f == 0:
                print(y, x, z, '|', f * 1)

# yxz