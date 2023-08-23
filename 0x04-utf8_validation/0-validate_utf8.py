#!/usr/bin/python3
"""utf8 validation Algorithm"""


from typing import List


def validUTF8(data: List[int]) -> bool:
    """utf8 validation"""
    numberOfBytes = 0

    for num in data:
        bin_rep = format(num, "08b")[-8:]

        if numberOfBytes == 0:
            for bit in bin_rep:
                if bit == "0":
                    break
                numberOfBytes += 1

            if numberOfBytes == 0:
                continue

            if numberOfBytes == 1 or numberOfBytes > 4:
                return False
        else:
            if not (bin_rep[0] == "1" and bin_rep[1] == "0"):
                return False

        numberOfBytes -= 1

    return numberOfBytes == 0
