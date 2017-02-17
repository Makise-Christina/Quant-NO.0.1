# simulate in a different way
# should we define it as a class?
import random

toBuy = {1:2,3:4}
toSel = {}

def tradeFinish(price):
    if toBuy.has_key(price) and toSel.has_key(price):
        nBuy = toBuy[price]
        nSel = toSel[price]
        if nBuy > nSel:
            pass

def tryBuy(price, amount, minSel):
    if price < minSel:
        if toBuy.has_key(price):
            toBuy[price] += amount
        else:
            toBuy[price] = amount
        return {price:amount}
    else:
        if toSel.has_key[minSel]:
            pass
