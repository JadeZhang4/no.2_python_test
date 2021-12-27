print('there are nothing')
amount = 230000
rate = 0.05

years = 50
year = 1
while year <= years:
    amount = amount * (1 + rate)
    print(f'第{year}年，本息合计{amount}元')
    year = year + 1
