def is_leap(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False

test_years = [2000, 2024, 1900, 2100]
for year in test_years:
    print(f'\{year\}: {'Leap year' if is_leap(year) else 'Not a leap year'})
