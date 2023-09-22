#!/usr/bin/python3
"""
Given a pile of coins of different values, determine the fewest number of
coins needed to meet a given amount total.
"""
from typing import List


def makeChange(coins, total):
    """changeCoin"""
    # Create a list called dp to store minimum coin counts for various totals.
    # Initialize all values in dp to be greater than the given total.
    dp = [total + 1] * (total + 1)

    # It takes 0 coins to make a total of 0.
    dp[0] = 0

    # Sort the available coins in ascending order.
    coins.sort()

    # Loop through each possible total from 1 to the given total.
    for t in range(1, total + 1):
        # Loop through each available coin value.
        for c in coins:
            # Check if the current coin can be used to make the current total.
            if t - c >= 0:
                # Update dp[t] with the minimum between its current value
                # and 1 + dp[t - c].
                dp[t] = min(dp[t], 1 + dp[t - c])
            else:
                # If the coin is too large to contribute to the current total,
                # break the loop.
                break

    # If dp[total] is still greater than the initial total
    # it means no valid combination of coins was found.
    # In this case, return -1 to indicate it's not possible.
    return dp[total] if dp[total] != total + 1 else -1
