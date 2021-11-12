def star(n):
    return "*" * n

stars_counts = [12, 6, 4, 9, 3]
adjust = len(str(max(stars_counts)))

for star_count in stars_counts:
    print(f"{str(star_count).rjust(adjust)}: {star(star_count)}")