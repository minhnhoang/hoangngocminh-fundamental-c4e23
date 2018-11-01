prices = {
    'banana': 4,
    'apple': 2,
    'orange': 1.5,
    'pear': 3,
}
stocks = {
    'banana': 6,
    'apple': 0,
    'orange': 32,
    'pear': 15,
}
total = 0
for i in prices.keys():
    print(i)
    print('price:', prices[i])
    print('stock:', stocks[i])
    total += prices[i] * stocks[i]
print("Total revenue:",total)