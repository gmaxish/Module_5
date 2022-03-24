years = 3
first_two_years = int((years - (years - 2)) * 10.5)
other = 4 * (years - 2)

if years >= 2:
    human_years = first_two_years + other
    print(human_years)
else:
    human_years = int(years * 10.5)
    print(human_years)
