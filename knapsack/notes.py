"""combinations are normally factorial"""

import random
import time
from itertools import combinations


class Item:
    def __init__(self, name, weight, value):
        self.name = name
        self.weight = weight
        self.value = value
        self.efficiency = 0

    def __str__(self):
        return f"{self.name}, {self.weight} lbs, ${self.value}"


small_cave = []
medium_cave = []
large_cave = []


def fill_cave_with_items():
    names = ["painting", "jewel", "coin", "statue", "treasure chest"]

    for _ in range(5):
        n = names[random.randint(0, 4)]
        w = random.randint(1, 25)
        v = random.randint(1, 100)
        small_cave.append(Item(n, w, v))

    for _ in range(15):
        n = names[random.randint(0, 4)]
        w = random.randint(1, 25)
        v = random.randint(1, 100)
        small_cave.append(Item(n, w, v))

    for _ in range(25):
        n = names[random.randint(0, 4)]
        w = random.randint(1, 25)
        v = random.randint(1, 100)
        small_cave.append(Item(n, w, v))


def print_results(items, knapsack):
    print("best items")
    print(f"{time.time()-start:.5f} seconds")
    print("---------")


def naive_fill_knapsack(sack, items):  # first pass
    """Put highest val items in a knapsack until full
    (other basic, native approaches exist)"""

    # TODO - sort items by value
    # sort in the highest to lowest order
    items.sort(key=lambda x: x.value, reversed=True)

    sack = []
    weight = 0

    # TODO - put the most valuable items in knapsack until full
    # determine weight of sack with new item, before adding to sack
    # check weight of sack

    for i in items:
        weight += i.weight
        if weight > 50:
            return sack
        else:
            sack.append(i)
    return sack

    # TODO- put most valuable items in knapsack until full
    # determin weight of sack with new item, before adding to sack
    # check weight of sack

# takes a long time to solve


def brute_force_knapsack(sack, items):
    # TODO - generate all possible
    combos = []
    sack = []
    for i in range(1, len(items)+1):
        list_ofcombos = list(combinations(items, i))

        for combo in list_ofcombos:
            combos.append(list(combo))

    # TODO - calculare the value of all combinations
    best_value = -1
    for c in combos:
        value = 0
        weight = 0
        for item in c:
            value += item.value
            weight += item.weight
        # find the combo with the highest value
        if weight <= 50 and value > best_value:
            best_value = value
            sack = c
    return sack

    # find the combo with the highest value


def greedy_fill_knapsack(sack, items):
    # calculate efficiency
    for i in items:
        i.efficiency = i.value//i.weight
    # sort items by efficientcy
    items.sort(key=lambda x: x.efficiency, reverse=True)
    # put items in knpasack until full

    sack = []
    weight = 0
    for i in items:
        weight += i.weight
        if weight > 50:
            return sack
        else:
            sack.append(i)
    return sack


fill_cave_with_items()
knapsack = []
print("Starting test 2, brute test")
items = medium_cave
start = time.time()
knapsack = brute_force_knapsack(knapsack, items)
print_results(items, knapsack)


print("Starting test 2, greedy test")
items = medium_cave
start = time.time()
greedy_fill_knapsack(knapsack, items)
print_results(items, knapsack)
