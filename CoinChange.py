def rec_coin(target, coin):
    min_coin = target
    if target in coin:
        return 1
    else:
        # for every coin value that is <= my target
        list = [c for c in coin if c <= target]
        for i in list:
            # add a coin count + recursive(new target, coin)
            num_coin = 1 + rec_coin(target-i, coin)

            # reset minimum if the new num_coins < minimun
            if num_coin < min_coin:
                min_coin = num_coin
    return min_coin


print(rec_coin(12, [1,5,10]))

def rec_coin_dynam(target, coins, known_results):
    # default output to target
    min_coins = target
    # base case
    if target in coins:
        known_results[target] = 1
    # return a known result if it happen to be greater than 1
    elif known_results[target] > 0:
        return known_results[target]
    else:
        for i in [c for c in coins if c <= target]:
            num_coins = 1 + rec_coin_dynam(target-i, coins, known_results)

            if num_coins < min_coins:
                min_coins = num_coins
                known_results[target] = min_coins
    return min_coins
target = 74
coins = [1,5,10,25]
known_results = [0] * (target+1)
print(rec_coin_dynam(target,coins, known_results))
