import sys
from typing import List, Dict


def _get_change(money: int,
                coins: List[int],
                memo: Dict[int, int]) -> int:
    """
    return the min number of coins required to
    make amount "money" from the given denominations
    of coins
    """

    if money < coins[min(len(coins) - 1, 1)]:
        return money
    else:

        min_coins = money  # can definitely make it from all 1s

        for c in coins:
            if c > money:
                # can't use this coin - too big
                continue
            else:
                remainder = money - c
                coins_required = memo.get(remainder)
                if coins_required is None:
                    # have not previously calculated value - work it out now
                    coins_required = 1 + _get_change(remainder, coins, memo)
                    memo.update({remainder: coins_required})

                # set min number of coins if less than current
                min_coins = min(min_coins, coins_required)

        return min_coins


def get_change(money: int,
               coins: List[int]) -> int:
    """
    return the min number of coins required to
    make amount "money" from the given denominations
    of coins
    """

    coins.sort()
    memo = dict()
    return _get_change(money, coins, memo)


if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m, [1, 3, 4]))
