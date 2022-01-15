# fractional  Kanapsack prroblem
class Item:
    def __init__(self, weight, value):
        self.weight = weight
        self.value = value
        self.ratio = value/weight


def knapsackMethod(items, capacity):
    items.sort(key=lambda x: x.ratio, reverse=True)
    used_capacity = 0
    total_value = 0
    for i in items:
        if used_capacity + i.weight <= capacity:
            used_capacity += i.weight
            total_value += i.value
        else:
            unused_weight = capacity - used_capacity
            value = i.ratio * unused_weight
            used_capacity += unused_weight
            total_value += value
        if used_capacity == capacity:
            break

    print("Total Value Obtained " + str(total_value))


item1 = Item(20, 100)
item2 = Item(30, 120)
item3 = Item(10, 60)

cList = [item1, item2, item3]
knapsackMethod(cList, 50)
