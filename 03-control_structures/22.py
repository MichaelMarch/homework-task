divisors_map = { 3 : "THREE", 5 : "FIVE" }

for i in range(1, 30 + 1):
    for key in divisors_map:
        if i % key == 0:
            print(divisors_map[key], end = ' ')
    else:
        print(i, end = ' ')