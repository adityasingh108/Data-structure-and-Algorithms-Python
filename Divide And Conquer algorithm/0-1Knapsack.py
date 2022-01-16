# solve 0 and 1 knapsack problem
class Item:
    def __init__(self, weight, profit):
        self.profit = profit
        self.weight = weight


def ZeroOneknapsack(items, capacity, current_index):
    if capacity <= 0 or current_index < 0 or current_index >= len(items):
        return 0
    elif items[current_index].weight <= capacity:
        profit1 = items[current_index].profit + ZeroOneknapsack(items, capacity-items[current_index].weight, current_index+1)
        profit2 = ZeroOneknapsack(items, capacity, current_index+1)
        return max(profit1, profit2)
    else:
        return 0


apple = Item(1, 26)
orange = Item(2, 17)
banana = Item(5, 72)
mango = Item(3, 31)

fruit_list = [apple, banana, mango, orange]


print(ZeroOneknapsack(fruit_list, 7, 0))
