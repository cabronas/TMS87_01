prices = [4,7,1,2]
maxProfit = 0
sortedBuyPrices = list(prices)
sortedBuyPrices.sort()
i = 0
for Buyindex, Buyprice in enumerate(sortedBuyPrices):
    j = len(prices)-1
    while prices.index(Buyprice) <= j:
            if prices[j] - Buyprice > maxProfit:
                maxProfit = prices[j] - Buyprice
            j -= 1
print(maxProfit)