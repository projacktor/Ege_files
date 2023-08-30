# special
maximum=0
for c1 in range(100):
    for c2 in range(100):
        for c3 in range(100):
            for c4 in range(100):
                if (c1 * 0 + c2 * 1 + c3 * 0 + c4 * 2 == 47 and c1 * 1 + c2 * 0 + c3 * 2 + c4 * 0 < 70) \
                        and (2 * c1 + c3 == 2 * c2 + c4):
                    if (c1 * 1 + c2 * 0 + c3 * 2 + c4 * 0) > maximum:
                        maximum = c1 * 1 + c2 * 0 + c3 * 2 + c4 * 0
print(maximum)
