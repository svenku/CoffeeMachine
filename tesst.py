eur_coins = {100: 20, 50: 20, 20: 0, 10: 0, 5: 2, 2: 15, 1: 1}


def get_change(amount, coins=eur_coins):
    change = []
    for denomination in sorted(coins.keys(), reverse=True):
        while denomination <= amount and coins[denomination] > 0:
            amount -= denomination
            coins[denomination] -= 1
            change.append(denomination)

    if amount != 0:
        raise Exception("Insufficient coins to give change")

    return change

print(get_change(49))
print(eur_coins)
