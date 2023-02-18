house_price = 1000000
good_credit = False

if good_credit:
    down_payment = int(house_price * 0.1)
else:
    down_payment = int(house_price * 0.2)
print(f'Down Payment: ${down_payment}')