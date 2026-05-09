"№ 27757Апробация04.03.26(Уровень: Базовый)"

for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                f = ((not x) and y and z and (not w)) or ((not x) and y and (not z) and (not w)) or (x and y and z and (not w))
                if f == 1:
                    print(x, w, z, y, '|', f * 1)
# xwzy