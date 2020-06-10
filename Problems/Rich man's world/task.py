a_client = int(input())
i_interest = 1.071
years = 0
while a_client < 700000:
    a_client = a_client * i_interest
    years += 1
print(years)
