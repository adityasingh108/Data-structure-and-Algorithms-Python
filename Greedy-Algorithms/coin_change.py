# coin change problem using greedy algorithm

def coinChange(totalNumber, coins):
    N = totalNumber
    coins.sort()
    index = len(coins) - 1
    while True:
        coinValue = coins[index]
        if N >= coinValue:
            print(coinValue)
            N = N-coinValue
        if N < coinValue:
            index -= 1
        if N == 0:
            break


coins = [1, 10, 20, 50, 100, 200, 500, 2000]
coinChange(425, coins)
