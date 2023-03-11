def is_leap_year(n):
    return n % 4 == 0 and (n % 100 != 0 or n % 400 == 0)


def next_leap_year(n):
    while not is_leap_year(n):
        n += 1
    return n


year = int(input("Year: "))
print(f"The next leap year after {year} is {next_leap_year(year + 1)}")
