from money import Money

cash = Money()


def get_change(amount, coins=cash.coins):
    change = []
    for denomination in sorted(coins.keys(), reverse=True):
        while denomination <= amount and coins[denomination]['count'] > 0:
            amount -= denomination
            coins[denomination]['count'] -= 1
            change.append(denomination)

    if amount != 0:
        raise Exception("Insufficient coins to give change")

    return change


print(get_change(49))
print(cash)
